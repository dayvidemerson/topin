# Generated by Django 2.0.1 on 2018-01-20 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0003_remove_marker_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='type',
            field=models.CharField(choices=[('bus_stop', 'Parada de ônibus'), ('ticket_store', 'Ponto de venda de passagens')], max_length=50, verbose_name='tipo'),
        ),
    ]
