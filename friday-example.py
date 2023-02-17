import time
import random
import sys
import board
import csv
import serial
import adafruit_bme680
from adafruit_pm25.uart import PM25_UART

uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.95)

reset_pin = None

pm25 = PM25_UART(uart, reset_pin)

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

start_time = int(time.time())
itime = start_time

run_time = int(sys.argv[1])

if (len(sys.argv) > 2):
    file_name = sys.argv[2]

print(file_name)
file = open(file_name,"w", newline='')
writer = csv.writer(file)
meta_data = ["Time","PM10","PM25","PM100","Temp","Gas","Relative Humidity","Pressure","Altitude"]
writer.writenow(meta_data)

while itime < (start_time + run_time):
    time.sleep(1)
    try:
        aqdata = pm25.read()
        # print(aqdata)
        itime = time.time()
        PM10 = aqdata["pm10 standard"]
        PM25 = aqdata["pm25 standard"]
        PM100 = aqdata["pm100 standard"]
        Temp = bme680.temperature
        Gas = bme680.gas
        RelHum = bme680.relative_humidity
        Press = bme680.pressure
        Alt = bme680.altitude
        data = [itime,PM10,PM25,PM100,Temp,Gas,RelHum,Press,Alt]
        
        writer.writerow(data)
        
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue













while True:
    time.sleep(1)

    try:
        aqdata = pm25.read()
        # print(aqdata)
        itime = time.time()
        PM10 = aqdata["pm10 standard"]
        PM25 = aqdata["pm25 standard"]
        PM100 = aqdata["pm100 standard"]
        
        data = [itime,PM10,PM25,PM100]
        
        writer.writerow(data)
        
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue