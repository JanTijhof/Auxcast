#!/usr/bin/env python
import RPi.GPIO as GPIO
import subprocess
import os
import time

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(3, GPIO.FALLING, bouncetime=300)
#	os.system("ifup wlan0")
	print ('script started succesfully')

def loop():
	while True:
		if GPIO.event_detected(3):
			print('Shutdown Button Pressed')
			time.sleep(0.5)
			if (GPIO.input(3) == False) :
				subprocess.call(['shutdown', '-h', 'now'], shell=False)
#				os.system("shutdown now -h")
#				shut down the Pi

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		GPIO.cleanup
#		print ('script for shutdown ended')
