from django.urls import path
from .views import (
    message_handle,
    getDataDevice,
    getGroup,
    getDevice,
    message_handle_v1,
    listDeviceGroups,
    listDevices,
    DeviceStats,
    edit_device,
    edit_device_group,
    get_graph_data,
)

urlpatterns = [
    path("v1/<str:imei>/", message_handle_v1, name="message"),
    path("group/<str:user_id>/", getGroup, name="getGroup"),
    path("data/<str:device_imei>/", getDataDevice, name="getDataDevice"),
    path("devices/<str:group_name>/", getDevice, name="getDeviceGroup"),
    path("device_groups/", listDeviceGroups, name="listDeviceGroups"),
    path("list_devices/<int:id>/", listDevices, name="listDevices"),
    path("device_stats/<int:id>/", DeviceStats, name="DeviceStats"),
    path("<str:imei>/", message_handle, name="message"),
    path("edit/device/<int:id>/", edit_device, name="edit_device"),
    path("edit/device-group/<int:id>/", edit_device_group, name="edit_device_group"),
    path("device/<int:id>/graph-data/", get_graph_data, name="get_graph_data"),
]
