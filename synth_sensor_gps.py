from pprint import pprint
import json
import argparse

class DataSynthesizer():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('gps_file')
        self.parser.add_argument('sensor_file')
        self.parser.add_arvument('-o', '--offset')
        self.parser.parse_args(namespace=self)
        if not self.offset:
            self.offset = 0.

    def line_generator(self, filename):
        with open(filename, 'r') as f_obj:
        for line in f_obj:
            yield line

    def pair_readings(self):
        gps_gen = self.line_generator(self.gps_file)
        sensor_gen = self.line_generator(self.sensor_file)
        for line in sensor_gen:
            sensor_data = json.loads(line)
            gps_reading = next(gps_gen)
