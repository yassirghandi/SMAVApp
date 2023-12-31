# Generated by Django 4.0.5 on 2023-06-25 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MessageStore', '0048_device_whatsapps_devicegroup_whatsapps_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='whatsapps',
        ),
        migrations.RemoveField(
            model_name='devicegroup',
            name='whatsapps',
        ),
        migrations.AlterField(
            model_name='data',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datas', to='MessageStore.device'),
        ),
        migrations.AlterField(
            model_name='devicegroup',
            name='devices',
            field=models.ManyToManyField(blank=True, related_name='device_groups', to='MessageStore.device', verbose_name='Device Group'),
        ),
    ]
