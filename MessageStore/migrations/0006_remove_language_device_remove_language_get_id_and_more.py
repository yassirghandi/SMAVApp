# Generated by Django 4.0.4 on 2022-06-08 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MessageStore', '0005_language_device_language_get_id_language_language_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='device',
        ),
        migrations.RemoveField(
            model_name='language',
            name='get_id',
        ),
        migrations.RemoveField(
            model_name='language',
            name='language',
        ),
        migrations.RemoveField(
            model_name='language',
            name='type',
        ),
    ]
