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
import pynmea2

#! HDC1080 Sensor
import sys
from modules import SDL_Pi_HDC1080

#! BMP280 Sensor
from mpu9250_jmdev.mpu_9250 import MPU9250
from mpu9250_jmdev.registers import *

#! EXTRA PACKAGES
import magic

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

class NEO: #! maintenance
    def read(self):
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=1)
        dataout = pynmea2.NMEAStreamReader()
        # newdata=ser.readline()

        # print("Data Type: ", type(ser))
        # print(ser)

        newdata = ser.readline().decode("utf-7")
        # newdata = ser.readline().split("$GPGGA,",1)[1]
        # newdata = (ser.readline()[2:].decode()).strip()

        # m = magic.Magic(mine_encoding=True)
        # encoding = m.from_buffer(newdata)
        # print(encoding)

        print("Data Type: ", type(newdata))
        print(newdata)

        if (newdata[0:6]) == ("$GPGGA"): # or GPGGA or GPRMC
            newmsg=pynmea2.parse(newdata)
            lat=newmsg.latitude
            lng=newmsg.longitude
            # gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
            return lat, lng

        else:
            # print(newdata[0:6])
            # print("<--------------------->")
            # print(str(newdata))
            # print("<--------------------->")
            # print(list(newdata))
            return "", ""

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
