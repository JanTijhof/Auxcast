#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import time


def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(4, GPIO.FALLING, bouncetime=300)
	print ('script started succesfully')

def loop():
#GPIO.add_event_detect(4, GPIO.FALLING)
#print ('script started succesfully')
	while True:
		if GPIO.event_detected(4):
			print('Casting Button Pressed')
			time.sleep(0.5)
			if (GPIO.input(4) == False) :
				os.system("go-chromecast -n 'Muziek' stop")
				time.sleep(0.2)
				os.system("go-chromecast -n 'Muziek' load http://192.168.1.169:8000/turntable.mp3")
				time.sleep(1)
				serial.write('\x03')
				print('script run, waiting for another button press')

if __name__ == '__main__':
	setup()

	try:
		loop()

	except KeyboardInterrupt:
		GPIO.cleanup
		print ('script for castingbutton ended')
