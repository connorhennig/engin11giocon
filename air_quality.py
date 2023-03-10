import time
import board
import csv

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

reset_pin = None

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

print("Found PM2.5 sensor, reading data...")

f = open("air_quality_data.csv","w", newline = '')

meta_data = ["Time","PM10","PM25","PM100"]

writer = csv.writer(f)

writer.writerow(meta_data)

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
        
    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")
