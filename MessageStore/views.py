from dataclasses import field
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from .models import DeviceGroup, Device
from .helper import (
    find_device,
    save_data,
    getUserGroup,
    getData,
    getAllDevice,
    save_data_v1,
)
from .forms import DeviceForm, DeviceGroupForm


@csrf_exempt
def message_handle(request, imei):
    if request.method == "POST":
        device = find_device(imei)
        if device is None:
            return HttpResponse("device not found")
        valid = save_data(request.body, device)
        if valid == 0:
            return HttpResponse("success")
        return HttpResponse("fail")
    return HttpResponse("ok")


@csrf_exempt
def message_handle_v1(request, imei):
    if request.method == "POST":
        device = find_device(imei)
        if device is None:
            return HttpResponse("device not found")
        valid = save_data_v1(request.body, device)
        if valid == 0:
            return HttpResponse("success")
        return HttpResponse("fail")
    return HttpResponse("ok")


# return group use own
def getGroup(request, user_id):
    groups = getUserGroup(user_id)
    data = serializers.serialize("json", groups, fields=("name", "description"))
    print(data)
    return HttpResponse(data, content_type="application/json")


# return data device
def getDataDevice(request, device_imei):
    item = getData(device_imei)

    data = serializers.serialize("json", item)

    return HttpResponse(data, content_type="application/json")


# return device in group
def getDevice(request, group_name):
    devices = getAllDevice(group_name)

    data = serializers.serialize("json", devices)
    print(data)

    return HttpResponse(data, content_type="application/json")


def listDeviceGroups(request):
    device_groups = []
    try:
        if request.user.whatsapp:
            device_groups = request.user.whatsapp.device_groups.all()
    except:
        pass
    return render(
        request, "dashboard/list_device_groups.html", {"device_groups": device_groups}
    )


def listDevices(request, id):
    device_group = get_object_or_404(DeviceGroup, id=id)
    devices = device_group.devices.all()
    return render(request, "dashboard/list_devices.html", {"devices": devices})


def DeviceStats(request, id):
    device = get_object_or_404(Device, id=id)
    return render(request, "dashboard/stats.html", {"device": device})


def edit_device(request, id):
    device = get_object_or_404(Device, id=id)
    form = DeviceForm(instance=device)
    if request.method == "POST":
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect("listDeviceGroups")
    return render(request, "dashboard/device_form.html", {"form": form})


def edit_device_group(request, id):
    group = get_object_or_404(DeviceGroup, id=id)
    form = DeviceGroupForm(instance=group)
    if request.method == "POST":
        form = DeviceGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("listDeviceGroups")
    return render(request, "dashboard/device_group_form.html", {"form": form})


def get_graph_data(request, id):
    hours = request.GET.get("hour", "24")
    try:
      hours = int(hours)
    except:
      hours = 24
    device = get_object_or_404(Device, id=id)
    data = {
      "temperature1_data": device.temperature1_data(hour=hours),
      "dew_point_data": device.dew_point_data(hours),
      "temperature2_data": device.temperature2_data(hours), 
      "dew_point2_data": device.dew_point2_data(hours),
      "gas_data": device.gas_data(hours),
      "wind_data": device.wind_data(hours),
      "battery_data": device.battery_data(hours),
      "machine_data": device.machine_data(hours),
    }
    return JsonResponse(data, safe=False)
