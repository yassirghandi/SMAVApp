from datetime import datetime

from rest_framework import serializers
from MessageStore.models import Device, DeviceGroup, Data, Language


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

    def to_representation(self, instance):
        # request = self.context['request']
        # print(request)
        data = super().to_representation(instance)
        latest_data = instance.latest_data
        data["temperature1"] = getattr(latest_data, "temperature1", None)
        data["temperature2"] = getattr(latest_data, "temperature2", None)
        data["dew_point"] = getattr(latest_data, "dew_point", None)
        data["dew_point2"] = getattr(latest_data, "dew_point2", None)
        data["humidity1"] = getattr(latest_data, "humidity1", None)
        data["humidity2"] = getattr(latest_data, "humidity2", None)
        data["wind"] = getattr(latest_data, "wind", None)
        data["gas"] = getattr(latest_data, "gas", None)
        data["voltage"] = getattr(latest_data, "voltage", None)
        data["machineStatus"] = getattr(latest_data, "machineStatus", None)
        data["signal"] = getattr(latest_data, "signal", None)
        data["windMax"] = instance.get_windMax
        data["windMin"] = instance.get_windMin
        data["alertsNumber"] = 0
        data["alerts_text"] = 'No alerts now'
        data['datetime'] = getattr(latest_data, "datetime", None)
        data['running_hours'] = '0 h 0 min'
        return data


class DeviceGroupSerializer(serializers.ModelSerializer):
    devices = DeviceDataSerializer(many=True)

    class Meta:
        model = DeviceGroup
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class LanguageAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            "gasWarning",
            "volWarning",
            "tempWarning",
            "inverWarning",
            "alarmStatus",
            "machineStart",
            "machineStop",
            "machineErorr",
            "machineWarning",
            "nowDevice",
            "online",
            "offline",
            "manual",
            "automatic",
        ]


class DeviceDataSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        selected_date = request.GET.get('selected_date', None)
        selected_hour = request.GET.get('selected_hour', None)
        if selected_date:
            selected_date = datetime.strptime(selected_date, "%d/%m/%Y")
            print(selected_date)
            if selected_hour:
                try:
                    selected_hour = int(selected_hour)
                except:
                    return {'error': 'selected_hour must be an integer value!'}
                latest_data = instance.latest_data_for_selected_date_and_hour(selected_date=selected_date,
                                                                              selected_hour=selected_hour)
            else:
                latest_data = instance.latest_data_for_selected_date(selected_date=selected_date)
            print(latest_data)
            if latest_data is None:
                return {'error': 'No data available for selected date!'}

        else:
            latest_data = instance.latest_data

        data = super().to_representation(instance)
        data["temperature1"] = getattr(latest_data, "temperature1", None)
        data["temperature2"] = getattr(latest_data, "temperature2", None)
        data["dew_point"] = getattr(latest_data, "dew_point", None)
        data["dew_point2"] = getattr(latest_data, "dew_point2", None)
        data["humidity1"] = getattr(latest_data, "humidity1", None)
        data["humidity2"] = getattr(latest_data, "humidity2", None)
        data["wind"] = getattr(latest_data, "wind", None)
        data["gas"] = getattr(latest_data, "gas", None)
        data["voltage"] = getattr(latest_data, "voltage", None)
        data["machineStatus"] = getattr(latest_data, "machineStatus", None)
        data["signal"] = getattr(latest_data, "signal", None)
        if selected_date:
            data["windMax"] = instance.get_windMax_by_date(selected_date=selected_date)
            data["windMin"] = instance.get_windMin_by_date(selected_date=selected_date)
        else:
            data["windMax"] = instance.get_windMax
            data["windMin"] = instance.get_windMin
        data["alertsNumber"] = 0
        data["alerts_text"] = 'No alerts now'
        data['datetime'] = getattr(latest_data, "datetime", None)
        data['running_hours'] = '0 h 0 min'
        return data
