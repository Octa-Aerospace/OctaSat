import picamera
import time

def capturephoto(imgname):
  with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.exif_tags['IFD0.Artist'] = 'Altaruru'
    camera.exif_tags['IFD0.Copyright'] = 'Copyright (c) 2019 Altaruru.com!'
    camera.exposure_compensation = 2
    time.sleep(2)
    camera.capture(imgname)
    camera.stop_preview()

capturephoto("captura1.jpg")

# Maybe we should just to use "os" python 3 library and take the picture directly from command line, then save it using a loop to change the name.