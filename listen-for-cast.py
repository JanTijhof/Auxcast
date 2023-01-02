#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
import time
import pychromecast

def setup():
	#Define the mode for GPIO pinout
	GPIO.setmode(GPIO.BCM)
	#Setup pin 4 as powered pin
	GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#Look for falling signal at pin 4, activated by pulling to ground
	GPIO.add_event_detect(4, GPIO.FALLING, bouncetime=300)
	print ('Auxcast is listening for button presses')

def loop():
	while True:
		if GPIO.event_detected(4):
			print('Auxcast - Casting Button Pressed')
			time.sleep(0.5)
			if (GPIO.input(4) == False) :
				# Discover and connect to chromecasts named Muziek
				chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=['Muziek'])
				[cc.device.friendly_name for cc in chromecasts]

				cast = chromecasts[0]
				# Start worker thread and wait for cast device to be ready
				cast.wait()
				print("Auxcast connected to:")
				print(cast.device)

				mc = cast.media_controller
				mc.play_media('http://192.168.1.169:8000/turntable.mp3', 'audio/mp3', stream_type="LIVE")
				mc.block_until_active()
				run_asap(mc, 0.1, 3)
				#print(mc.status)
				print('Auxcast - Connected, waiting for another button press')

def run_asap(receiver, interval, blast_duration):
	count = int(blast_duration/interval)
	for i in range(count):
		time.sleep(interval)
		receiver.play()

if __name__ == '__main__':
	setup()

	try:
		loop()

	except KeyboardInterrupt:
		GPIO.cleanup
#	print ('Auxcast - script for castingbutton ended')


