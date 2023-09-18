# Generated by Django 4.0.5 on 2023-07-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageStore', '0050_device_whatsapps_devicegroup_whatsapps'),
        ('webhooks', '0009_whatsapp_device_groups_whatsapp_devices_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsapp',
            name='device_groups',
            field=models.ManyToManyField(blank=True, related_name='whatsapps_groups', to='MessageStore.devicegroup', verbose_name='Device Groups'),
        ),
        migrations.AlterField(
            model_name='whatsapp',
            name='devices',
            field=models.ManyToManyField(blank=True, related_name='whatsapps_device', to='MessageStore.device', verbose_name='Devices'),
        ),
    ]