from modules.OctaSat import OctaSat

OctaSat = OctaSat()

if __name__ == '__main__':
    while True:
        try:
            OctaSat.start()

        except OSError:
            print('\n[ ! ] Warning: OSError, running anyways :).\n')

        except KeyboardInterrupt:
            print("\n[ ! ] Exiting\n")
            exit()
