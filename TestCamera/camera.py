import picamera as pc
import time

camera = pc.PiCamera()

def take_picture(num):
    camera.capture("/home/pi/TestCamera/pictures/image_{}.jpg".format(num))

for i in range(1, 11):
    take_picture(i)

# This already works and can provide a timelapse
