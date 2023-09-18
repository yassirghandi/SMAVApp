# Generated by Django 4.0.5 on 2022-06-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatsapp',
            name='alertStatus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='whatsapp',
            name='lastmessage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='whatsapp',
            name='machineVoltage',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='whatsapp',
            name='temperatureAlert',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='whatsapp',
            name='language',
            field=models.CharField(default='English', max_length=15),
        ),
    ]
