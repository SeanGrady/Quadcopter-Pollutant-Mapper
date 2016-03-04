# Aerial Atmospheric Impurity Vehicle

The goal of this project is to provide an airborne sensing and mapping platform for a prototype air quality sensor.

This repository will contain the code to read data from the sensor and pilot the quadcopter accordingly, in order to acomplish tasks such as finding sources of pollutants or mapping the air quality across a region.

The airframe currently being used is a Parrot AR.Drone 2.0, which we have modified with the Paparazzi open source autopilot software. 

To receive sensor data on the RPi 2:
  1. pair the RPi 2 with the sensor (HC-06) and make sure it's trusted
  2. run 'sdptool add sp'
  3. run 'sudo rfcomm bind /dev/rfcomm1 <bluetooth address (i.e. 20:15:05:04:32:55)>
  4. run read_sensor_data.py

To synthesize the data, run
synth_sensor_gps.py <flight log filename> <sensor data log filename>

for example:
synth_sensor_gps.py 16_03_02__16_51_49.data sensor_log.txt
