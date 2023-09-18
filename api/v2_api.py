from datetime import datetime

from django.http import Http404, HttpResponseBadRequest
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from MessageStore.models import Device
from api.serializers import DeviceDataSerializerV2


class DeviceDetailAPIVieV2(RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Device.objects.all()
    serializer_class = DeviceDataSerializerV2

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_object(self):
        farm_id = self.kwargs['farmId']
        device_imei = self.kwargs['deviceImei']
        selected_date = self.request.GET.get('selected_date', None)
        if selected_date:
            try:
                selected_date = datetime.strptime(selected_date, "%d/%m/%Y")
            except Exception as e:
                raise Http404()
        try:
            device = Device.objects.get(device_groups__id=farm_id, imei=device_imei)
        except:
            raise Http404()

        return device
        # if getattr(self.request.user, "whatsapp", None):
        #     whatsapp = self.request.user.whatsapp
        #     devices_access = whatsapp.devices.filter(id=device.id).exists()
        #     device_group_access = whatsapp.device_groups.filter(devices__id=device.id).exists()
        #     if devices_access or device_group_access:
        #         return device
        #
        # raise Http404()
