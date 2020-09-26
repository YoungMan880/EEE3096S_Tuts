import time
import RPi.GPIO as GPIO

# pin defenitions
btn_pin = 4
led_pin = 12

# Set pin warning sto false
GPIO.setwarnings(False)
# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set setup pins
GPIO.setup(btn_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

# If Button is pushed light up LED
try:
	while True:
		if GPIO.input(btn_pin):
			GPIO.output(led_pin, GPIO.LOW)
		else:
			GPIO.output(led_pin, GPIO.HIGH)

# When you press ctrl+c, this will be called
finally:
	GPIO.cleanup()
