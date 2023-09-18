# Generated by Django 4.0.5 on 2023-05-23 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageStore', '0047_remove_device_whatsapps_remove_devicegroup_whatsapps'),
        ('webhooks', '0006_whatsapp_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatsapp',
            name='device_groups',
            field=models.ManyToManyField(blank=True, related_name='whatsapps', to='MessageStore.devicegroup', verbose_name='WhatsApp User'),
        ),
        migrations.AddField(
            model_name='whatsapp',
            name='devices',
            field=models.ManyToManyField(blank=True, related_name='whatsapps', to='MessageStore.device', verbose_name='WhatsApp User'),
        ),
    ]