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
        except Exception as e:
            with open("/home/pi/OctaSat/data/error_log.txt", "a+") as file:
<<<<<<< HEAD
                file.write("{0} at {1}\n\n".format(e, OctaSat.Time()))
=======
                file.write("{0} at {1}\n".format(e, OctaSat.Time()))
>>>>>>> 39727a35187c3335ba048180a5cf79b4a4d0f9ca
            os.system("sudo reboot")
