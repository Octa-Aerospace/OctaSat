from time import sleep
from datetime import datetime as dt
from modules.mainModule import NEO, HDC, BMP, MPU, Buzzer
from modules.transceiver import LORA
from data.OctaCSV import OctaCSV as oc


class OctaSat:
    def __init__(self):
        self.NEO = NEO()
        self.HDC = HDC()
        self.BMP = BMP()
        self.MPU = MPU()
        self.Buzzer = Buzzer(pin=18)
        self.LORA = LORA()
        self.oc = oc()

    def NEO_read(self):
        return self.NEO.read()  # * lat, lon

    def HDC_read(self):
        return self.HDC.read(decimal=2)  # * temp, hum

    def BMP_read(self):
        return self.BMP.read(decimal=2)  # * temp, press, alt

    def MPU_read(self):
        return self.MPU.read()  # * accel, gyros, magnet

    def Buzzer_beep(self):
        self.Buzzer.beep_on()
        sleep(0.5)  # ! if we put this sleep, that will affect the module's reads
        self.Buzzer.beep_off()
        sleep(2)  # ! same the above
        return '[ ok ] Successfully beeped'

    def LORA_send(self, data):
        self.LORA.send(data)
        return '[ ok ] Successfully sent'

    def Time(self):
        now = dt.now()
        return now.strftime('%d/%m, %H:%M:%S')

    def black_box(self, file_name, data):
        self.oc.header(file_name=file_name, headers=list(data.keys()))
        self.oc.writer(file_name=file_name, data=list(data.values()))
        return '[ ok ] Successfully saved'

    def start(self):
        # latitude, longitude = self.NEO_read() #! maintenance
        hdc_temperature, humidity = self.HDC_read()
        bmp_temperature, pressure, altitude = self.BMP_read()
        self.Buzzer_beep()  # * just beep

        data = {
            # 'latitude': latitude, #! maintenance
            # 'longitude': longitude, #! maintenance
            'hdc_temperature': hdc_temperature,
            'bmp_temperature': bmp_temperature,
            'humidity': humidity,
            'pressure': pressure,
            'altitude': altitude,
            'time': self.Time()
        }

        self.black_box(file_name='./data/OctaCSV.csv', data=data)

        # * formating payload ready to send
        payload = self.LORA.prepare_payload(data)
        # * send payload and return the confimation
        print(payload)
        print(self.LORA_send(payload))
