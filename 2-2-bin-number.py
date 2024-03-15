import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

nums = [255, 127, 64, 32, 5, 0, 256]

def bin_translator(num):
    number = [0 for i in range(len(dac))] # fill with 0

    d_num = num % 256                     # prevent overflow

    bin_num = bin(d_num)                  # turn into bin

    i = -1                                # set i to go from end to start
    while bin_num[i] != 'b':
        number[i] = int(bin_num[i])       # fill in the array
        i -= 1
    
    print('{} => {}'.format(num, number))

    GPIO.output(dac, number)
    volt = float(input())
    voltage.append(volt)

    return

voltage = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for i in nums:
    bin_translator(i)

print(voltage)

GPIO.outpu(dac, 0)
GPIO.cleanup()