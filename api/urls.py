from django.urls import path

from .v2_api import DeviceDetailAPIVieV2
from .views import (
    FarmListAPIView,
    FarmDetailAPIView,
    FarmDevicesAPIView,
    DeviceDetailAPIView,
    DeviceDataAPIView,
    DataHistoryAPIView,
    AlertAPIView,
)

urlpatterns = [
    path('api/farms', FarmListAPIView.as_view(), name='farm-list'),
    path('api/farms/<int:pk>', FarmDetailAPIView.as_view(), name='farm-detail'),
    path('api/farms/<int:farmId>/devices', FarmDevicesAPIView.as_view(), name='farm-devices'),
    path('api/farms/<int:farmId>/devices/<str:deviceImei>', DeviceDetailAPIView.as_view(), name='device-detail'),
    path('postdata/data/<str:deviceImei>', DeviceDataAPIView.as_view(), name='device-data'),
    path('api/data/history/<int:device_imei>/', DataHistoryAPIView.as_view(), name='data-history'),
    path('api/alerts/<str:name>/', AlertAPIView.as_view(), name='AlertAPIView'),

    path('api/v2/farms/<int:farmId>/devices/<str:deviceImei>', DeviceDetailAPIVieV2.as_view(), name='device-data-v2'),

]
