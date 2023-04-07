import RPi.GPIO as GPIO
import datetime
import time
import csv
import sys

channel = 17

count = 0
mincount = 0

run_time = int(sys.argv[1])

interval = float(sys.argv[2])

if (len(sys.argv) > 3):
    file_name = sys.argv[3]
    
print(file_name)
file = open(file_name,"w", newline='')
writer = csv.writer(file)
meta_data = ["Time","Counts"]
writer.writerow(meta_data)

def my_callback(channel):
    global count 
    count += 1
    global mincount 
    mincount += 1
    print('Radiation detected at ' + str(datetime.datetime.now())) 

start_time = time.time()

while ((time.time() - start_time) <= run_time):
    current_time = time.time()
    while (( time.time() - current_time ) <= interval):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(channel, GPIO.FALLING, callback= my_callback, bouncetime=50)
        except:
            pass
    print('{} counts in {} seconds'.format(mincount,interval))
    current_time = time.time()
    data = [current_time,mincount]
    writer.writerow(data)
    mincount = 0

file.close()
