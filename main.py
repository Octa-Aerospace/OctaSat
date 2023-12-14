from time import sleep
#
from modules.Buzzer import Buzzer
from modules.Camera import Camera
from modules.GY91 import GY91
# from modules.E32 import E32
# from modules.GPS import GPS

class OctaSat:
  def __init__(self):
    self.BUZZER_PIN = 12
    self.I2C_ADDRESS = 0x68
  
  def init(self):
    self.gy91 = GY91(self.I2C_ADDRESS)
    self.camera = Camera()
    # self.e32 = E32()

    self.buzzer = Buzzer(self.BUZZER_PIN)
    self.buzzer.init()

  def read_data(self):
    accel = self.gy91.get_accel()
    gyro = self.gy91.get_gyro()
    mag = self.gy91.get_mag()

    print(f"Accelerometer: {accel.x} {accel.y} {accel.z}")
    print(f"Gyroscope: {gyro.x} {gyro.y} {gyro.z}")
    print(f"Magnetometer: {mag.x} {mag.y} {mag.z}")
    print("\n")
    # latitude, longitude, altitude = self.gps.read_data()
    pass

  def save_data(self):
    pass

  def send_data(self):
    pass

  def kill(self):
    self.buzzer.destroy()

if __name__ == "__main__":
  device = OctaSat()
  device.init()

  for i in range(5):
    device.read_data()
    sleep(1)

  device.kill()
