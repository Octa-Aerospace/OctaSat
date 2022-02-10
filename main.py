import os
import datetime
from modules.OctaSat import OctaSat

OctaSat = OctaSat()

if __name__ == '__main__':
    while True:
        try:
            OctaSat.start()

        # except OSError:
        #     # print("\n[ ! ] Warning: OSError detected, rebooting system.\n")
        #
        #     os.system("sudo reboot") #* the error should be added to the csv file

        except KeyboardInterrupt:
            print("\n[ ! ] Exiting\n")
            exit()

        # for unknown errors
        # except Exception as e:
        #     with open("/home/pi/OctaSat/data/error_log.txt", "a+") as file:
        #         file.write("{0} at {1}\n".format(e, OctaSat.Time()))
        #     os.system("sudo reboot")
