# Generated by Django 2.0.1 on 2018-01-27 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0006_insert_values_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='markers',
            field=models.ManyToManyField(blank=True, to='route.Marker', verbose_name='marcadores'),
        ),
    ]
