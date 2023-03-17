import RPi.GPIO as GPIO
import datetime
import time

channel = 16

count = 0
mincount = 0

def my_callback():
    count = count + 1
    mincount = mincount + 1
    print('Radiation detected at ' + str(datetime.datetime.now())) 

while True:
    current_time = time.time()
    while (( time.time() - current_time ) <= 60):
        try:
            #GPIO.setmode(GPIO.BCM)
            GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(channel, GPIO.FALLING, callback=my_callback, bouncetime=100)
        except:
            pass
    print('CPM is {}'.format(mincount))
    mincount = 0
