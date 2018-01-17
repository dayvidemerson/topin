# Generated by Django 2.0.1 on 2018-01-17 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='type',
            field=models.CharField(choices=[('bus_stop', 'parada de ônibus'), ('ticket_store', 'ponto de venda de passagens')], default='bus_stop', max_length=50, verbose_name='tipo'),
            preserve_default=False,
        ),
    ]