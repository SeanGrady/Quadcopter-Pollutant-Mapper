import serial
from pprint import pprint
import json

class DataReceiver():
    def __init__(self):
        self.serial_speed = 9600
        self.serial_port = '/dev/tty.HC-06-DevB'
        self.connection = serial.Serial(
                self.serial_port,
                self.serial_speed,
                timeout=1
        )
        with open('sensor_log.txt', 'w') as wipe:
            pass
        print self.connection.isOpen()

    def read_data_stream(self):
        try:
            while True:
                latest_raw = self.connection.readline()
                if latest_raw:
                    latest_readings = json.loads(latest_raw)
                    self.parse_data(latest_readings)
                else:
                    print "No data packet"
        except KeyboardInterrupt:
            pass

    def parse_data(self, data_object):
        pprint(data_object)
        with open('sensor_log.txt', 'a') as infile:
            json.dump(data_object, infile)
            infile.write('\n')

if __name__ == "__main__":
    dr = DataReceiver()
    dr.read_data_stream()
