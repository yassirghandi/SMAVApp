# Generated by Django 4.0.5 on 2023-07-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0009_whatsapp_device_groups_whatsapp_devices_and_more'),
        ('MessageStore', '0049_remove_device_whatsapps_remove_devicegroup_whatsapps_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='whatsapps',
            field=models.ManyToManyField(blank=True, related_name='whatsapps_device', to='webhooks.whatsapp', verbose_name='WhatsApp Users'),
        ),
        migrations.AddField(
            model_name='devicegroup',
            name='whatsapps',
            field=models.ManyToManyField(blank=True, related_name='whatsapps_groups', to='webhooks.whatsapp', verbose_name='WhatsApp User'),
        ),
    ]
