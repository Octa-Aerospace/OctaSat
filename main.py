#
from modules.Buzzer import Buzzer
from modules.Camera import Camera

PIN_BUZZER = 12

if __name__ == "__main__":
  buzzer = Buzzer(PIN_BUZZER)
  buzzer.play_startup()
  buzzer.destroy()
