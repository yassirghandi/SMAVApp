from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from MessageStore.models import Device, DeviceGroup, Data, Language
from .serializers import DeviceSerializer, DeviceGroupSerializer, DeviceDataSerializer, DataSerializer, \
    LanguageAlertSerializer


class FarmListAPIView(generics.ListAPIView):
    serializer_class = DeviceGroupSerializer

    def get_queryset(self):
        if getattr(self.request.user, "whatsapp", None):
            return DeviceGroup.objects.filter(whatsapps__id=self.request.user.whatsapp.id)
        return DeviceGroup.objects.none()


class FarmDetailAPIView(generics.RetrieveAPIView):
    serializer_class = DeviceGroupSerializer

    def get_object(self):
        device_group_pk = self.kwargs.get("pk", None)
        if getattr(self.request.user, "whatsapp", None):
            return get_object_or_404(DeviceGroup, whatsapps__id=self.request.user.whatsapp.id, pk=device_group_pk)
        raise Http404()


class FarmDevicesAPIView(generics.ListAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        farm_id = self.kwargs['farmId']
        print(farm_id)
        print(self.request.user.whatsapp.id)
        try:
            whatsapps_id = self.request.user.whatsapp
        except:
            raise Http404()
        try:
            device_group = DeviceGroup.objects.get(id=farm_id)
        except Exception as e:
            raise Http404()
        return Device.objects.filter(device_groups__id=farm_id)  # whatsapps_device__id=self.request.user.whatsapp.id
        # if device_group.whatsapps == self.request.user.whatsapp:
        #     # return Device.objects.filter(device_groups__id=farm_id) # whatsapps_device__id=self.request.user.whatsapp.id
        # else:
        #     raise Http404()


class DeviceDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Device.objects.all()
    # serializer_class = DeviceSerializer
    serializer_class = DeviceDataSerializer

    def get_object(self):
        farm_id = self.kwargs['farmId']
        device_imei = self.kwargs['deviceImei']
        try:
            device = Device.objects.get(device_groups__id=farm_id, imei=device_imei)
        except:
            raise Http404()
        if getattr(self.request.user, "whatsapp", None):
            whatsapp = self.request.user.whatsapp
            devices_access = whatsapp.devices.filter(id=device.id).exists()
            device_group_access = whatsapp.device_groups.filter(devices__id=device.id).exists()
            if devices_access or device_group_access:
                return device

        raise Http404()


class DeviceDataAPIView(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceDataSerializer
    lookup_field = "imei"
    lookup_url_kwarg = "deviceImei"

    def get_object(self):
        device_imei = self.kwargs['deviceImei']
        device = Device.objects.filter(imei=device_imei).first()
        if not device:
            raise Http404()

        if getattr(self.request.user, "whatsapp", None):
            whatsapp = self.request.user.whatsapp
            devices_access = whatsapp.devices.filter(id=device.id).exists()
            device_group_access = whatsapp.device_groups.filter(devices__id=device.id).exists()
            if devices_access or device_group_access:
                return device

        # return JsonResponse({"error": "You dont have access"}, status=401)
        raise Http404()


class DataPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DataHistoryAPIView(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    pagination_class = DataPagination

    def get_queryset(self):
        device_imei = self.kwargs['device_imei']
        device = get_object_or_404(Device, imei=device_imei)
        queryset = device.get_all_data()
        return queryset


class AlertAPIView(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageAlertSerializer
    lookup_field = "name"
    lookup_url_kwarg = "name"
