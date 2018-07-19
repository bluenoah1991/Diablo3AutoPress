#!/usr/bin/env python3

import sys, time

INPUT_CHANNEL = 11

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("RPi.GPIO module not found.")
    sys.exit(1)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(INPUT_CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print('Start wait signal')

while True:
    channel = GPIO.wait_for_edge(INPUT_CHANNEL, GPIO.RISING, timeout=5000)
    if channel is None:
        print('Timeout occurred')
    else:
        print('Edge detected on channel %s' % channel)
    time.sleep(0.2)

GPIO.cleanup()

