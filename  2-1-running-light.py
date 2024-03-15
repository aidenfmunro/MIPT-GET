import RPi.GPIO as GPIO
import time

leds = [9, 10, 22, 27, 17, 4, 3, 2]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

n = 5

for i in range(n):
    for j in range(len(leds)):

        GPIO.output(leds[j], 1)

        time.sleep(0.2)

        GPIO.output(leds[j], 0)

GPIO.output(leds, 0)
GPIO.cleanup()
