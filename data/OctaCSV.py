import csv
import os

class OctaCSV:
    def header(self, file_name, headers):
        header_exist = os.path.isfile(file_name)

        with open(file_name, 'r+', newline='') as file:
            if header_exist:
                write = csv.writer(file)
                write.writerow(headers)

    def writer(self, file_name, data):
        with open(file_name, 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
