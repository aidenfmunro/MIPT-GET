import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

n = 10

pwm = GPIO.PWM(24, 1000)

pwm.start(0)

try:
    while True:
        f = int(input())

        pwm.ChangeDutyCycle(f)

        print(3.3 * f / 100)

finally:
    pwm.stop()
    GPIO.output(24, 0)
    GPIO.cleanup()