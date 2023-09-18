# Generated by Django 4.0.5 on 2023-06-25 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MessageStore', '0049_remove_device_whatsapps_remove_devicegroup_whatsapps_and_more'),
        ('webhooks', '0008_remove_whatsapp_device_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatsapp',
            name='device_groups',
            field=models.ManyToManyField(blank=True, related_name='whatsapps', to='MessageStore.devicegroup', verbose_name='Device Groups'),
        ),
        migrations.AddField(
            model_name='whatsapp',
            name='devices',
            field=models.ManyToManyField(blank=True, related_name='whatsapps', to='MessageStore.device', verbose_name='Devices'),
        ),
        migrations.AddField(
            model_name='whatsapp',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whatsapp', to=settings.AUTH_USER_MODEL),
        ),
    ]