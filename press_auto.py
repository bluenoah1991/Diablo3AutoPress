#!/usr/bin/env python3

import sys, time, random

INPUT_CHANNEL = 11

NULL_CHAR = chr(0)

char_table = {
    'a': 4, 'b': 5, 'c': 6, 'd': 7, 'e': 8, 'f': 9,
    'g': 10, 'h': 11, 'i': 12, 'j': 13, 'k': 14, 'l': 15,
    'm': 16, 'n': 17, 'o': 18, 'p': 19, 'q': 20, 'r': 21,
    's': 22, 't': 23, 'u': 24, 'v': 25, 'w': 26, 'x': 27,
    'y': 28, 'z': 29, '1': 30, '2': 31, '3': 32, '4': 33,
    '5': 34, '6': 35, '7': 36, '8': 37, '9': 38, '0': 39,
    'ret': 40, ' ': 44,
}

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def write_report_with_release(report):
    write_report(report)
    write_report(NULL_CHAR*8)

def write_char(ch):
    if ch in char_table:
        deccode = char_table[ch]
        write_report_with_release(
            NULL_CHAR * 2 + chr(deccode) + NULL_CHAR * 5)

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("RPi.GPIO module not found.")
    sys.exit(1)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(INPUT_CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Random press 1, 2, 3, 4

SWITCH_FLAG = [False,]

def gpio_callback(channel):
    global SWITCH_FLAG
    SWITCH_FLAG[0] = not SWITCH_FLAG[0]

GPIO.add_event_detect(INPUT_CHANNEL, GPIO.RISING, callback=gpio_callback, bouncetime=200)

chs = ['1', '2', '3', '4']

while True:
    random.shuffle(chs)
    for ch in chs:
        # random sleep 157ms to 250ms
        ts = random.randint(157, 250)
        if SWITCH_FLAG[0]:
            write_char(ch)
        time.sleep(ts / 1000.0)

GPIO.cleanup()

