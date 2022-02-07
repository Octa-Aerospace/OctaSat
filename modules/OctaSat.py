import os
from time import sleep
from datetime import datetime as dt
import picamera
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
        self.Camera = picamera.PiCamera()
        self.LORA = LORA()
        self.oc = oc()

    def NEO_read(self):
        # return self.NEO.read()  # * lat, lon, alt, sat
        return self.NEO.coordinates() # lat, lon, alt

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

    def Camera_Shot(self, num=1, route="/home/pi/OctaSat/data/images/"):
        while True:
            if not os.path.isfile(route + "shot_{}".format(num) + ".jpg"):
                self.Camera.capture(route + "shot_{}".format(num) + ".jpg")
                break
            else:
                num += 1

        return '[ ok ] Successfully shot'

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
        # latitude, longitude, neo_altitude, num_satellites = self.NEO_read() #! maintenance
        latitude, longitude, neo_altitude = self.NEO_read()
        hdc_temperature, humidity = self.HDC_read()
        bmp_temperature, pressure, mpu_altitude = self.BMP_read()
        self.Buzzer_beep() # * just beep

        data = {
            'latitude': latitude, #! maintenance
            'longitude': longitude, #! maintenance
            'neo_altitude': neo_altitude, #! maintenance
            # 'num_satellites': num_satellites, #! maintenance
            # 'latitude': latitude, #! maintenance
            # 'longitude': longitude, #! maintenance
            'hdc_temperature': hdc_temperature,
            'bmp_temperature': bmp_temperature,
            'humidity': humidity,
            'pressure': pressure,
            'mpu_altitude': mpu_altitude,
            'time': self.Time()
        }

        # save data in OBC memory
        print(self.black_box(file_name='/home/pi/OctaSat/data/OctaCSV.csv', data=data))

        # take a picture
        print(self.Camera_Shot())

        # * formating payload ready to send
        payload = self.LORA.prepare_payload(data)

        print(self.LORA_send(payload))
        print(payload, end="\n\n")
