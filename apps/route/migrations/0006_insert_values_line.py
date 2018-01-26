import json

from django.db import migrations
from django.conf import settings


def forwards_func(apps, schema_editor):
    Line = apps.get_model("route", "Line")
    PointLine = apps.get_model("route", "PointLine")
    User = apps.get_model("authtools", "User")
    db_alias = schema_editor.connection.alias
    user = User.objects.get(pk=1)
    filepath = '{}/apps/route/fixtures/lines.json'.format(settings.BASE_DIR)
    data = json.load(open(filepath))

    for value in data:
        line = Line(name=value['name'], slug=value['slug'], description=value['description'])
        line.user = user
        line.save()

    lines = Line.objects.all()

    filepath = '{}/apps/route/fixtures/points.json'.format(settings.BASE_DIR)
    points = json.load(open(filepath))

    for point in points:
        PointLine.objects.using(db_alias).create(
            line=lines.get(slug=point['line']),
            latitude=point['latitude'],
            longitude=point['longitude'],
            order=point['order']
        )


def reverse_func(apps, schema_editor):
    Line = apps.get_model("route", "Line")
    PointLine = apps.get_model("route", "PointLine")
    db_alias = schema_editor.connection.alias
    lines = json.loads(open('{}/apps/route/fixtures/lines.json'.format(settings.BASE_DIR)))

    for line in lines:
        PointLine.objects.using(db_alias).filter(line__slug=line['slug']).delete()
        Line.objects.using(db_alias).filter(slug=line['slug']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0005_auto_20180125_0055')
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
