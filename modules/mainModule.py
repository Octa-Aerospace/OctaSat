from subprocess import PIPE
from bmp280 import BMP280

#! BPM280 Sensor
try:
    from smbus2 import SMBus

except ImportError:
    from smbus import SMBus

#! Buzzer Module
import RPi.GPIO as GPIO
from time import sleep

#! NEO6M Module
from datetime import *
import serial
# import pynmea2

#! HDC1080 Sensor
import sys
from modules import SDL_Pi_HDC1080

#! BMP280 Sensor
from mpu9250_jmdev.mpu_9250 import MPU9250
from mpu9250_jmdev.registers import *

#! EXTRA PACKAGES
# import magic

class BMP:
    def __init__(self):
        # Initialize the BMP280
        self.bus = SMBus(1)
        self.bmp280 = BMP280(i2c_dev=self.bus)

    def temp(self, decimal):
        temperature = round(self.bmp280.get_temperature(), decimal)
        return temperature

    def press(self, decimal):
        pressure = round(self.bmp280.get_pressure(), decimal)
        return pressure

    def alt(self, decimal):
        baseline_values = []
        baseline_size = 100

        # Calibration with 100 sampling
        for i in range(baseline_size):
            baseline_values.append(round(self.bmp280.get_pressure(), 4))

        baseline = sum(baseline_values[:-25]) / len(baseline_values[:-25])
        altitude = round(self.bmp280.get_altitude(qnh=baseline), decimal)
        return altitude

    def read(self, decimal):
        return self.temp(decimal), self.press(decimal), self.alt(decimal)

class Buzzer:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def beep_on(self):
        GPIO.output(self.pin, True)

    def beep_off(self):
        GPIO.output(self.pin, False)

class NEO:
    def __init__(self):
        self.mport = "/dev/ttyAMA0"

    def get(self):
        ser = serial.Serial(self.mport, 9600, timeout=2)
        # print(str(ser.readline()))
        # print(ser.readline().decode(errors="ignore"))

        return str(ser.readline())
        # return str(ser.readline().decode(errors="ignore"))

    def split_data(self):
        data = self.get()
        for i in range(len(data)):
            if data[i] == "G" and data[i+4] == "A":
                # print(data[i:i+5])
                data = data[i:-5]
                break
        while data[0:5] != "GPGGA":
            # print(data)
            data = self.get()
            for i in range(len(data)):
                if data[i] == "G" and data[i+4] == "A":
                    # print(data[i:i+5])
                    data = data[i:-5]
                    break
            # print(data)
            if data[0:5] == "GPGGA":
                self.data = data.split(",")
                # print(self.data)
                self.name = "Global Postioning System Fix Data"
                self.current_utc_time = data[1]
                self.latitude_deg = self.data[2] # + self.data[3]
                self.longitude_deg = self.data[4] # + self.data[5]
                self.num_satellites = self.data[7]
                self.horizontal_dilution_pos = self.data[8]
                self.altitude = self.data[9]

                data = [
                    self.latitude_deg,
                    self.longitude_deg,
                    self.altitude,
                    self.num_satellites,
                    self.horizontal_dilution_pos,
                ]

                return data
            else:
                print("GPGGA DON'T MATCH")

        if data[0:5] == "GPGGA":
            self.data = data.split(",")
            # print(self.data)
            self.name = "Global Postioning System Fix Data"
            self.current_utc_time = data[1]
            self.latitude_deg = self.data[2] # + self.data[3]
            self.longitude_deg = self.data[4] # + self.data[5]
            self.num_satellites = self.data[7]
            self.horizontal_dilution_pos = self.data[8]
            self.altitude = self.data[9]

            data = [
                self.latitude_deg,
                self.longitude_deg,
                self.altitude,
                self.num_satellites,
                self.horizontal_dilution_pos,
            ]

            return data

        if data[0:5] == "GPGGA":
            self.data = data.split(",")
            # print(self.data)
            self.name = "Global Postioning System Fix Data"
            self.current_utc_time = data[1]
            self.latitude_deg = self.data[2] # + self.data[3]
            self.longitude_deg = self.data[4] # + self.data[5]
            self.num_satellites = self.data[7]
            self.horizontal_dilution_pos = self.data[8]
            self.altitude = self.data[9]

            data = [
                self.latitude_deg,
                self.longitude_deg,
                self.altitude,
                self.num_satellites,
                self.horizontal_dilution_pos,
            ]

            return data

        if data[0:5] == "GPGGA":
            self.data = data.split(",")
            # print(self.data)
            self.name = "Global Postioning System Fix Data"
            self.current_utc_time = data[1]
            self.latitude_deg = self.data[2] # + self.data[3]
            self.longitude_deg = self.data[4] # + self.data[5]
            self.num_satellites = self.data[7]
            self.horizontal_dilution_pos = self.data[8]
            self.altitude = self.data[9]

            data = [
                self.latitude_deg,
                self.longitude_deg,
                self.altitude,
                self.num_satellites,
                self.horizontal_dilution_pos,
            ]

            return data

        if data[0:5] == "GPGGA":
            self.data = data.split(",")
            # print(self.data)
            self.name = "Global Postioning System Fix Data"
            self.current_utc_time = data[1]
            self.latitude_deg = self.data[2] # + self.data[3]
            self.longitude_deg = self.data[4] # + self.data[5]
            self.num_satellites = self.data[7]
            self.horizontal_dilution_pos = self.data[8]
            self.altitude = self.data[9]

            data = [
                self.latitude_deg,
                self.longitude_deg,
                self.altitude,
                self.num_satellites,
                self.horizontal_dilution_pos,
            ]

            return data

    def decoder(self, coord):
        l = list(coord)
        for i in range(0,len(l)-1):
                if l[i] == "." :
                        break
<<<<<<< HEAD
        try:
            base = l[0:i-2]
            degi = l[i-2:i]
            degd = l[i+1:]
            baseint = int("".join(base))
            degiint = int("".join(degi))
            degdint = float("".join(degd))
            degdint = degdint / (10**len(degd))
            degs = degiint + degdint
            full = float(baseint) + (degs/60)
            return full
        except:
            return None
=======
        base = l[0:i-2]
        degi = l[i-2:i]
        degd = l[i+1:]
        baseint = int("".join(base))
        degiint = int("".join(degi))
        degdint = float("".join(degd))
        degdint = degdint / (10**len(degd))
        degs = degiint + degdint
        full = float(baseint) + (degs/60)

        return full
>>>>>>> df1aa42bdccac7502a6d5cb6503a6278522629c6

    def coordinates(self):
        lat = self.decoder(self.split_data()[0])
        lon = self.decoder(self.split_data()[1])

<<<<<<< HEAD
        if lat != None or lon != None:
            return -lat, -lon
        else:
            return "", ""
=======
        return -lat, -lon
>>>>>>> df1aa42bdccac7502a6d5cb6503a6278522629c6

    def full_data(self):
        obj = {
            "latitude": self.coordinates()[0],
            "longitude": self.coordinates()[1],
            "altitude": self.split_data()[2],
            "num_satellites": self.split_data()[3],
            "horizontal_dilution_pos": self.split_data()[4],
        }

        return obj

    def read(self): # this is just to make OctaSat.py more readable
        data = self.full_data()
        latitude = data["latitude"]
        longitude = data["longitude"]
        altitude = data["altitude"]
        num_satellites = data["num_satellites"]

        return [latitude, longitude, altitude, num_satellites]

class HDC:
    def __init__(self):
        sys.path.append('./modules/SDL_Pi_HDC1080_Python3')
        self.hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()

    def temp(self, decimal):
        temperature = round(self.hdc1080.readTemperature(), decimal)
        return temperature

    def hum(self, decimal):
        humidity = round(self.hdc1080.readHumidity(), decimal)
        return humidity

    def read(self, decimal):
        temp = self.temp(decimal)
        hum = self.hum(decimal)
        return temp, hum

class MPU:
    def __init__(self):
        self.mpu = MPU9250(
            address_ak=AK8963_ADDRESS,
            address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
            address_mpu_slave=None,
            bus=1,
            gfs=GFS_1000,
            afs=AFS_8G,
            mfs=AK8963_BIT_16,
            mode=AK8963_MODE_C100HZ)
        self.mpu.configure()

    def accel(self):
        accelerometer = self.mpu.readAccelerometerMaster()

        #Accelerometer sorted values if [0][1][2] are X,Y,Z axis respectively
        xA = round(accelerometer[0], 6)
        yA = round(accelerometer[1], 6)
        zA = round(accelerometer[2], 6)
        outA = [xA, yA, zA]

        return outA

    def gyros(self):
        gyroscope = self.mpu.readGyroscopeMaster()

        #Gyroscope sorted values if [0][1][2] are X,Y,Z axis respectively
        xG = round(gyroscope[0], 6)
        yG = round(gyroscope[1], 6)
        zG = round(gyroscope[2], 6)
        outG = [xG, yG, zG]

        return outG

    def magnet(self):
        magnetometer = self.mpu.readMagnetometerMaster()

        #Magnetometer sorted values if [0][1][2] are X,Y,Z axis respectively
        xM = round(magnetometer[0], 6)
        yM = round(magnetometer[1], 6)
        zM = round(magnetometer[2], 6)
        outM = [xM, yM, zM]

        return outM

    def read(self, decimal):
        accel = self.accel(decimal)
        gyros = self.gyros(decimal)
        magnet = self.magnet(decimal)
        return accel, gyros, magnet
