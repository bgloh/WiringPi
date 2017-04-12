# Python-wrapper for wiring.io
# Apr.12, 2017
# blink test

#### HOW TO INSTALL 	wiringpi2
# sudo apt-get update
# sudo apt-get install python-dev python-pip
# sudo pip install wiringpi2

import wiringpi as wire
import time

# Raspberry Pi board revision
wire.piBoardRev()

pin = 7; #pin number
HIGH = 1; LOW = 0;
wire.wiringPiSetup(); #setup
wire.pinMode(pin,HIGH)
for i in range(0,100):
  wire.digitalWrite(pin,HIGH)
  time.sleep(0.5)
  wire.digitalWrite(pin, LOW)
  time.sleep(0.5)
  print('blinking :%d' %i)

