import RPi.GPIO as GPIO
from time import sleep
from matplotlib import pyplot as plt
import numpy as np

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

def dec2bin(num):
    number = [0 for i in range(len(dac))] # fill with 0

    d_num = num % 256                     # prevent overflow

    bin_num = bin(d_num)                  # turn into bin

    i = -1                                # set i to go from end to start
    while bin_num[i] != 'b':
        number[i] = int(bin_num[i])       # fill in the array
        i -= 1

    return number

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

carry_flag = 1
x = 0

try:
    period = float(input("Type a period for signal: "))

    while True:
        GPIO.output(dac, dec2bin(x))

        if   x == 0:    carry_flag = 1
        elif x == 255:  carry_flag = 0

        x = x + 1 if carry_flag == 1 else x - 1

        sleep(period / 512)

except ValueError:
    print("Inapropriate period!")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")
    