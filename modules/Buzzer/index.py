import RPi.GPIO as GPIO
from time import sleep
from sys import exit

class Buzzer:
  _global = None

  def __init__(self, pin):
    self.pin = pin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.pin, GPIO.OUT)
    self.pwm = GPIO.PWM(self.pin, 1)

  def play_startup(self):
    for frequency in [440, 523, 659, 880]:  # These frequencies correspond to A4, C5, E5, A5
      self.play_tone(frequency, 0.1)  # Play each tone for 0.1 seconds
      sleep(0.05)  # A short pause between notes

    self.play_tone(880, 1)  # A5 for 1 second

  def destroy(self):
    print("[!] Buzzer -- cleaning up GPIO")
    GPIO.cleanup(self.pin)

