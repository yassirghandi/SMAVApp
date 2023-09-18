from datetime import datetime
from django.db import models
from django.db.models import Max, Min

from webhooks.models import SmsUser, Whatsapp
import django


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=15)
    chat_id = models.CharField(max_length=15)
    language = models.CharField(max_length=15, default="English")
    country = models.CharField(max_length=15, default="")
    alertStatus = models.IntegerField(default=0, editable=False)
    temperatureAlert = models.IntegerField(default=1)
    machineVoltage = models.IntegerField(default=12)
    lastmessage = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Telegram User"
        verbose_name = "Telegram User"


class Language(models.Model):
    name = models.CharField(max_length=15)
    temperature1 = models.CharField(max_length=15)
    humidity1 = models.CharField(max_length=15)
    temperature2 = models.CharField(max_length=15)
    humidity2 = models.CharField(max_length=15)
    wind = models.CharField(max_length=15)
    gas = models.CharField(max_length=15)
    voltage = models.CharField(max_length=15)
    machineStatus = models.CharField(max_length=15)
    gasWarning = models.CharField(max_length=30, default="")
    volWarning = models.CharField(max_length=30, default="")
    tempWarning = models.CharField(max_length=30, default="")
    inverWarning = models.CharField(max_length=30, default="")
    alarmStatus = models.CharField(max_length=30, default="Alarm")
    machineStart = models.CharField(max_length=30, default="")
    machineStop = models.CharField(max_length=30, default="")
    machineErorr = models.CharField(max_length=30, default="")
    machineWarning = models.CharField(max_length=30, default="")
    wellcome = models.CharField(max_length=30, default="Welcome to SMAV")
    smavGroup = models.CharField(max_length=30, default="SMAV Group")
    smavSetting = models.CharField(max_length=30, default="SMAV Setting")
    selectSmav = models.CharField(max_length=30, default="Select a SMAV")
    smavList = models.CharField(max_length=30, default="SMAV List")
    chooseSmav = models.CharField(max_length=30, default="Choose SMAV")
    chooseLanguage = models.CharField(max_length=30, default="Choose Language")
    setAlarm = models.CharField(max_length=30, default="Set Alarm")
    request = models.CharField(max_length=30, default="Request")
    chooseRequest = models.CharField(max_length=30, default="Choose Request")
    generalState = models.CharField(max_length=30, default="General State")
    temperatureState = models.CharField(max_length=30, default="Temperature")
    windState = models.CharField(max_length=30, default="Wind")
    gasState = models.CharField(max_length=30, default="Gas")
    machineState = models.CharField(max_length=30, default="Machine State")
    maintainer = models.CharField(max_length=30, default="Maintainer")
    timeActive = models.CharField(max_length=30, default="Time Active")
    maintainerMenu = models.CharField(max_length=24, default="Maintainer")
    timeActiveMenu = models.CharField(max_length=24, default="Time Active")
    locationMenu = models.CharField(max_length=24, default="Location")
    informationMenu = models.CharField(max_length=24, default="Device Information")
    volSolarMenu = models.CharField(max_length=24, default="Voltage Solar")
    volSolar = models.CharField(max_length=30, default="Voltage Battery")
    volBatMenu = models.CharField(max_length=24, default="Voltage Battery")
    volBat = models.CharField(max_length=30, default="Voltage Solar")
    modeMenu = models.CharField(max_length=24, default="Mode")
    mode = models.CharField(max_length=30, default="Mode")
    signalDeviceMenu = models.CharField(max_length=24, default="Signal Quality")
    signalDevice = models.CharField(max_length=30, default="Signal Quality")
    temperatureH1 = models.CharField(max_length=30, default="Temperature Humide 1")
    temperatureH2 = models.CharField(max_length=30, default="Temperature Humide 2")
    online = models.CharField(max_length=30, default="Online")
    offline = models.CharField(max_length=30, default="Offline")
    nowDevice = models.CharField(max_length=30, default="Now device")
    manual = models.CharField(max_length=30, default="Manual")
    automatic = models.CharField(max_length=30, default="Automatic")
    excellentSignal = models.CharField(max_length=30, default="Excellent Signal")
    goodSignal = models.CharField(max_length=30, default="Good Signal")
    acceptableSignal = models.CharField(max_length=30, default="Acceptable Signal")
    weakSignal = models.CharField(max_length=30, default="Weak signal")


class Device(models.Model):
    name = models.CharField(max_length=15)
    imei = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20, default="")
    latitude = models.CharField(max_length=20, default="")
    timeActive = models.CharField(max_length=20, default="0", editable=True)
    maintainer = models.CharField(max_length=20, default="")
    contactMaintainer = models.CharField(max_length=150, default="")
    timeMaintain = models.DateTimeField(default=django.utils.timezone.now)
    active = models.IntegerField(default=0, editable=True)
    status = models.IntegerField(default=0, editable=False)
    timeStart = models.DateTimeField(default=django.utils.timezone.now, editable=False)
    clients = models.ManyToManyField(Client, blank=True, verbose_name="Telegram Users")
    whatsapps = models.ManyToManyField(
        Whatsapp, blank=True, verbose_name="WhatsApp Users", related_name="whatsapps_device"
    )
    sms = models.ManyToManyField(SmsUser, blank=True, verbose_name="SMS Users")

    class Meta:
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.imei

    @property
    def latest_data(self):
        try:
            return self.datas.all().order_by("-datetime")[0]
        except:
            return {}

    def latest_data_for_selected_date(self, selected_date):
        try:
            return self.datas.filter(datetime__date=selected_date).order_by("-id")[0]
        except:
            return None

    def latest_data_for_selected_date_and_hour(self, selected_date, selected_hour):
        try:
            return self.datas.filter(datetime__date=selected_date, datetime__hour=selected_hour).order_by("-id")[0]
        except:
            return None

    @property
    def get_windMax(self):
        try:
            max_wind = self.datas.filter(datetime__date=datetime.now().date()).aggregate(Max('wind'))
            if max_wind['wind__max'] != None:
                print(max_wind['wind__max'])
                return max_wind['wind__max']
            else:
                return 0
        except Exception as e:
            print(e)
            return 0

    @property
    def get_windMin(self):
        try:
            min_wind = self.datas.filter(datetime__date=datetime.now().date()).aggregate(Min('wind'))
            if min_wind['wind__min'] != None:
                print(min_wind['wind__min'])
                return min_wind['wind__min']
            else:
                return 0
        except Exception as e:
            print(e)
            return 0

    # @property
    def get_windMax_by_date(self, selected_date):
        try:
            max_wind = self.datas.filter(datetime__date=selected_date).aggregate(Max('wind'))
            if max_wind['wind__max'] != None:
                print(max_wind['wind__max'])
                return max_wind['wind__max']
            else:
                return 0
        except Exception as e:
            print(e)
            return 0

    # @property
    def get_windMin_by_date(self, selected_date):
        try:
            min_wind = self.datas.filter(datetime__date=selected_date).aggregate(Min('wind'))
            if min_wind['wind__min'] != None:
                print(min_wind['wind__min'])
                return min_wind['wind__min']
            else:
                return 0
        except Exception as e:
            print(e)
            return 0

    def get_all_data(self):
        try:
            return self.datas.all().order_by("-datetime")
        except:
            return []

    def gas_data(self, hour=6):
        return self.get_data(self.id, 'gas', hour)

    def wind_data(self, hour=6):
        return self.get_data(self.id, 'wind', hour)

    def battery_data(self, hour=6):
        return self.get_data(self.id, 'voltage', hour)

    def machine_data(self, hour=6):
        return self.get_machine_data(self.id, hour)

    def dew_point_data(self, hour=6):
        return self.get_dew_point_data(self.id, 1, hour)

    def dew_point2_data(self, hour=6):
        return self.get_dew_point_data(self.id, 1, hour)

    def temperature2_data(self, hour=6):
        return self.get_temperature_data(self.id, 2, hour)

    @property
    def temperature1_data(self, hour=6):
        return self.get_temperature_data(self.id, 1, hour)

    def temperature2_data(self, hour=6):
        return self.get_temperature_data(self.id, 2, hour)

    @staticmethod
    def get_temperature_data(device_id, num, hours=6):
        current_time = datetime.now()
        field = "temperature1"
        if num == 2:
            field = "temperature2"
        device = Device.objects.get(id=device_id)
        data = []

        for hour in range(0, hours):
            hour_data = []
            day = current_time.day
            hour = current_time.hour - hour
            if (hour) < 0:
                hour = 23 - abs(hour)
                day = day - 1
            minutes_data = device.datas.filter(
                datetime__year=current_time.year,
                datetime__month=current_time.month,
                datetime__day=day,
                datetime__hour=hour,
            ).values_list(field, flat=True)
            if not len(minutes_data) > 0:
                hour_data.append(0)
            else:
                hour_data.append(minutes_data[0])
            data += hour_data
            # for i in range(6):
        return data[::-1]

    @staticmethod
    def get_dew_point_data(device_id, num, hours=6):
        current_time = datetime.now()
        device = Device.objects.get(id=device_id)
        data = []

        for hour in range(0, hours):
            hour_data = []
            day = current_time.day
            hour = current_time.hour - hour
            if (hour) < 0:
                hour = 23 - abs(hour)
                day = day - 1
            minutes_data = device.datas.filter(
                datetime__year=current_time.year,
                datetime__month=current_time.month,
                datetime__day=day,
                datetime__hour=hour,
            )
            if not len(minutes_data) > 0:
                hour_data.append(0)
            else:
                if num == 2:
                    hour_data.append(minutes_data[0].dew_point2)
                else:
                    hour_data.append(minutes_data[0].dew_point)
            data += hour_data
        return data[::-1]

    @staticmethod
    def get_data(device_id, field, hours=6):
        current_time = datetime.now()
        device = Device.objects.get(id=device_id)
        data = []

        for hour in range(0, hours):
            hour_data = []
            day = current_time.day
            hour = current_time.hour - hour
            if (hour) < 0:
                hour = 23 - abs(hour)
                day = day - 1
            minutes_data = device.datas.filter(
                datetime__year=current_time.year,
                datetime__month=current_time.month,
                datetime__day=day,
                datetime__hour=hour,
            )
            if not len(minutes_data) > 0:
                hour_data.append(0)
            else:
                hour_data.append(getattr(minutes_data[0], field))
            data += hour_data

        return data[::-1]

    @staticmethod
    def get_machine_data(device_id, hours=6):
        current_time = datetime.now()
        device = Device.objects.get(id=device_id)
        data = []

        for hour in range(0, hours):
            hour_data = []
            day = current_time.day
            hour = current_time.hour - hour
            if (hour) < 0:
                hour = 23 - abs(hour)
                day = day - 1
            minutes_data = device.datas.filter(
                datetime__year=current_time.year,
                datetime__month=current_time.month,
                datetime__day=day,
                datetime__hour=hour,
            )
            if not len(minutes_data) > 0:
                hour_data.append(0)
            else:
                if minutes_data[0].machineStatus >= 12:
                    hour_data.append(1)
                else:
                    hour_data.append(0)
            data += hour_data
        return data[::-1]


class Data(models.Model):
    temperature1 = models.FloatField(max_length=5)
    humidity1 = models.FloatField(max_length=5)
    temperature2 = models.FloatField(max_length=5)
    humidity2 = models.FloatField(max_length=5)
    wind = models.FloatField(max_length=5)
    gas = models.FloatField(max_length=5)
    voltage = models.FloatField(default=0)
    mode = models.FloatField(default=0)
    signal = models.FloatField(default=0)
    machineStatus = models.FloatField(default=0)
    volBat = models.FloatField(default=0)
    temperatureH1 = models.FloatField(max_length=5, default=0)
    temperatureH2 = models.FloatField(max_length=5, default=0)

    datetime = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="datas")

    def __str__(self):
        return self.device.name

    class Meta:
        verbose_name_plural = "Datas"

    @property
    def dew_point(self):
        dew_point = self.temperature1 - ((100 - self.humidity1) / 5)
        return round(dew_point, 2)

    @property
    def dew_point2(self):
        dew_point = self.temperature2 - ((100 - self.humidity2) / 5)
        return round(dew_point, 2)


class DeviceGroup(models.Model):
    name = models.CharField(max_length=25, verbose_name="SMAV Group Name")
    devices = models.ManyToManyField(Device, blank=True, verbose_name="Device Group", related_name="device_groups")
    description = models.CharField(max_length=100, default="")
    whatsapps = models.ManyToManyField(
        Whatsapp, blank=True, verbose_name="WhatsApp User", related_name="whatsapps_groups"
    )
    clients = models.ManyToManyField(Client, blank=True, verbose_name="Telegram User")

    class Meta:
        verbose_name_plural = "Device Group"

    def __str__(self):
        return self.name
