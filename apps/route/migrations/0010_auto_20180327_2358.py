# Generated by Django 2.0.1 on 2018-03-28 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0009_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='back',
        ),
        migrations.RemoveField(
            model_name='route',
            name='city',
        ),
        migrations.RemoveField(
            model_name='route',
            name='front',
        ),
        migrations.RemoveField(
            model_name='route',
            name='user',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]
