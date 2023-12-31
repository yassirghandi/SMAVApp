# Generated by Django 4.0.5 on 2022-10-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webhooks", "0005_smsuser"),
        ("MessageStore", "0043_language_acceptablesignal_language_automatic_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="sms",
            field=models.ManyToManyField(
                blank=True, to="webhooks.smsuser", verbose_name="SMS Users"
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="active",
            field=models.IntegerField(default=0),
        ),
    ]
