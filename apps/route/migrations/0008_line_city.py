# Generated by Django 2.0.1 on 2018-02-18 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('route', '0007_line_markers'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.City', verbose_name='cidade'),
            preserve_default=False,
        ),
    ]
