from modules.OctaSat import OctaSat
import os

OctaSat = OctaSat()

if __name__ == '__main__':
    while True:
        try:
            OctaSat.start()

        except OSError:
            # print("\n[ ! ] Warning: OSError detected, rebooting system.\n")

            os.system("sudo reboot") #* the error should be added to the csv file
        except KeyboardInterrupt:
            print("\n[ ! ] Exiting\n")
            exit()

        except:
            os.system("sudo reboot") # this should be registered too
