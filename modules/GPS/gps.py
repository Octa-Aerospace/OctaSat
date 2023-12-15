import serial
import pynmea2

class GPS:
    def __init__(self):
        self.ser = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)

    def get_data(self):
      line = self.ser.readline().decode('utf-8')
      msg = pynmea2.parse(line)

      try:
        while True:
          if isinstance(msg, pynmea2.types.talker.GGA):
              return msg.latitude, msg.longitude, msg.altitude
          elif isinstance(msg, pynmea2.types.talker.GLL):
              return msg.latitude, msg.longitude, None  
      except pynmea2.ParseError as e:
          print(f'Error parsing NMEA sentence: {e}')
