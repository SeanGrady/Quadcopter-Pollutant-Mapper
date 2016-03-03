from pprint import pprint
import json
import argparse

class DataSynthesizer():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('gps_file')
        self.parser.add_argument('sensor_file')
        self.parser.add_argument('-o', '--offset')
        self.parser.parse_args(namespace=self)
        if not self.offset:
            self.offset = 0.

    def line_generator(self, filename):
        with open(filename, 'r') as f_obj:
            for line in f_obj:
                yield line

    def find_next_gps_line(self, gps_gen):
        while True:
            gps_reading = next(gps_gen)
            gps_data = gps_reading.strip().split()
            if gps_data[2] != "GPS_INT":
                continue
            else:
                return gps_data

    def pair_readings(self):
        gps_gen = self.line_generator(self.gps_file)
        sensor_gen = self.line_generator(self.sensor_file)
        for line in sensor_gen:
            sensor_data = json.loads(line)
            sensor_time = sensor_data['ts']
            gps_data = self.find_next_gps_line(gps_gen)
            gps_time = gps_data[0]
            lat = float(gps_data[6])
            lon = float(gps_data[7])
            lat = lat / 10000000
            lon = lon / 10000000
            print lat, lon, gps_time, sensor_time

if __name__ == "__main__":
    ds = DataSynthesizer()
    ds.pair_readings()
