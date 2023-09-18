from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Whatsapp(models.Model):
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="whatsapp", null=True, blank=True
    )
    language = models.CharField(max_length=15, default="English")
    alertStatus = models.CharField(max_length=15, default="ON", editable=False)
    temperatureAlert = models.IntegerField(default=1)
    machineVoltage = models.IntegerField(default=12)
    lastmessage = models.IntegerField(default=0, editable=False)
    devices = models.ManyToManyField(
        "MessageStore.Device", blank=True, verbose_name="Devices", related_name="whatsapps_device"
    )
    device_groups = models.ManyToManyField(
        "MessageStore.DeviceGroup", blank=True, verbose_name="Device Groups", related_name="whatsapps_groups"
    )

    class Meta:
        verbose_name_plural = "Whatsapp User"
        verbose_name = "Whatsapp User"

    def __str__(self):
        return self.name

    @property
    def get_user(self):
        if self.user:
            return self.user
        return None


class SmsUser(models.Model):
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    language = models.CharField(max_length=15, default="English")
    alertStatus = models.CharField(max_length=15, default="ON", editable=False)
    temperatureAlert = models.IntegerField(default=1)
    machineVoltage = models.IntegerField(default=12)
    lastmessage = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "SMS User"
        verbose_name = "SMS User"
