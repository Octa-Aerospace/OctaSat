import serial
# from OctaSat.modules.mainModule import Buzzer

class NEO:
    def __init__(self):
        self.mport = "/dev/ttyAMA0"

    def get(self):
        ser = serial.Serial(self.mport, 9600, timeout=2)
        # print(str(ser.readline()))
        # print(ser.readline().decode(errors="ignore"))

        return str(ser.readline())
        # return str(ser.readline().decode(errors="ignore"))

    def split_data(self):
        data = ""
        while data[0:5] != "GPGGA":
            # print(data)
            data = self.get()
            for i in range(len(data)):
                if data[i] == "G" and data[i+4] == "A":
                    # print(data[i:i+5])
                    data = data[i:-5]
                    break
            # print(data)
            if data[0:5] == "GPGGA":
                self.data = data.split(",")
                # print(self.data)
                self.name = "Global Postioning System Fix Data"
                self.current_utc_time = data[1]
                self.latitude_deg = self.data[2] # + self.data[3]
                self.longitude_deg = self.data[4] # + self.data[5]
                self.num_satellites = self.data[7]
                self.horizontal_dilution_pos = self.data[8]
                self.altitude = self.data[9]

                data = [
                    self.latitude_deg,
                    self.longitude_deg,
                    self.altitude,
                    self.num_satellites,
                    self.horizontal_dilution_pos,
                ]

                return data

    def decoder(self, coord):
        l = list(coord)
        for i in range(0,len(l)-1):
                if l[i] == "." :
                        break
        base = l[0:i-2]
        degi = l[i-2:i]
        degd = l[i+1:]
        baseint = int("".join(base))
        degiint = int("".join(degi))
        degdint = float("".join(degd))
        degdint = degdint / (10**len(degd))
        degs = degiint + degdint
        full = float(baseint) + (degs/60)

        return full

    def coordinates(self):
        lat = self.decoder(self.split_data()[0])
        lon = self.decoder(self.split_data()[1])
        alt = float(self.split_data()[2])
        # sat = int(self.split_data()[3]) # this increase the receive time in 2 secs

        return -lat, -lon, alt

    def full_data(self):
        obj = {
            "latitude": self.coordinates()[0],
            "longitude": self.coordinates()[1],
            "altitude": self.split_data()[2],
            "num_satellites": self.split_data()[3],
            "horizontal_dilution_pos": self.split_data()[4],
        }

        return obj

    def read(self): # this is just to make OctaSat.py more readable
        data = self.full_data()
        latitude = data["latitude"]
        longitude = data["longitude"]
        altitude = data["altitude"]
        num_satellites = data["num_satellites"]

        return [latitude, longitude, altitude, num_satellites]

if __name__ == "__main__":
    neo = NEO()
    # print("[ ok ] NEO INSTANCE")
    while True:
        # print("[ loop ]")
        # print(neo.split_data())
        print(neo.coordinates())
        # print(neo.full_data())
        # print(neo.read())
