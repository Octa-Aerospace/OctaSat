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
<<<<<<< HEAD
        # except Exception as e:
        #     with open("/home/pi/OctaSat/data/error_log.txt", "a+") as file:
        #         file.write("{0} at {1}\n".format(e, OctaSat.Time()))
        #     os.system("sudo reboot")
=======
        except Exception as e:
            with open("/home/pi/OctaSat/data/error_log.txt", "a+") as file:
                file.write("{0} at {1}\n".format(e, OctaSat.Time()))
            os.system("sudo reboot")
>>>>>>> df1aa42bdccac7502a6d5cb6503a6278522629c6
