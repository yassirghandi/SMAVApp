from django import forms
from .models import DeviceGroup, Device


class DeviceGroupForm(forms.ModelForm):
    class Meta:
        model = DeviceGroup
        fields = [
            "name",
        ]


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            "name",
        ]
