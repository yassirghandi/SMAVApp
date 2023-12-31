# Generated by Django 4.0.5 on 2023-02-19 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("webhooks", "0005_smsuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="whatsapp",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="whatsapp",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
