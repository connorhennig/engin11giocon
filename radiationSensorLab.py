import RPi.GPIO as GPIO
import datetime


channel = 16

count = 0
mincount = 0

def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        count = count + 1
        print('Radiation detected at ' + str(datetime.datetime.now())) 
while 
  try:
      #GPIO.setmode(GPIO.BCM)
      GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.add_event_detect(channel, GPIO.FALLING, callback=my_callback, bouncetime=200)
  
finally:
    GPIO.cleanup()
 
print("Goodbye!")
