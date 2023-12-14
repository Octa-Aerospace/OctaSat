#
from modules.Buzzer import Buzzer
from modules.Camera import Camera
# from modules.GY91 import GY91
# from modules.E32 import E32
# from modules.GPS import GPS

class OctaSat:
  def __init__(self):
    BUZZER_PIN = 12
    self.buzzer = Buzzer(BUZZER_PIN)
    self.camera = Camera()
    # self.gy91 = GY91()
    # self.e32 = E32()
    
  def read_data(self):
    # accel = self.gy91.get_accel()
    # gyro = self.gy91.get_gyro()
    # mag = self.gy91.get_mag()
    # latitude, longitude, altitude = self.gps.read_data()
    pass
    
  def save_data(self):
    pass
    
  def send_data(self):
    pass

if __name__ == "__main__":
  pass