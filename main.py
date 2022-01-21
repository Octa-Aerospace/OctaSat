from modules.OctaSat import OctaSat
import os

OctaSat = OctaSat()

if __name__ == '__main__':
    while True:
        try:
            OctaSat.start()

        # except OSError:
        #     print('\n[ ! ] Warning: OSError, running anyways :).\n')
        #
        #     print("\n[ ! ] Warning: OSError detected, rebooting system.\n")
        #     obs: rebot the system can be touble with image names (fit it)
        #     os.system("reboot") #* the error should be added to the csv file

        except TypeError:
            print("GPS data failed")

        except KeyboardInterrupt:
            print("\n[ ! ] Exiting\n")
            exit()
