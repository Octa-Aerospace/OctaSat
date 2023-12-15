from time import sleep
#
from modules.Buzzer import Buzzer
from modules.Camera import Camera
from modules.GY91 import GY91
from modules.GPS import GPS
# from modules.E32 import E32

class OctaSat:
  def __init__(self):
    self.BUZZER_PIN = 12
    self.I2C_ADDRESS = 0x68
  
  def init(self):
    self.gy91 = GY91(self.I2C_ADDRESS)
    self.camera = Camera()
    self.gps = GPS()
    # self.e32 = E32()

    self.buzzer = Buzzer(self.BUZZER_PIN)
    self.buzzer.init()
    
    data = self.read_data()
    self.save_data(data)
    self.send_data()
    self.kill()

  def read_data(self):
    accel = self.gy91.get_accel()
    gyro = self.gy91.get_gyro()
    mag = self.gy91.get_mag()
    latitude, longitude, altitude = self.gps.get_data()
    
    with open('data/data.csv', '+a') as file:
      file.write(f"{accel},{gyro},{mag},{latitude},{longitude},{altitude}\n")
    
    return {
      'accel': accel,
      'gyro': gyro,
      'mag': mag,
      'latitude': latitude,
      'longitude': longitude,
      'altitude': altitude,
    }

  def save_data(self, data):
    with open('data/data.csv', '+a') as file:
      file.write(f"{data['accel']},{data['gyro']},{data['mag']},{data['latitude']},{data['longitude']},{data['altitude']}\n")

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
