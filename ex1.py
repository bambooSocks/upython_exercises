from machine import Pin
import time

# setup of the button and the LED
led = Pin(13, Pin.OUT)
btn = Pin(14, Pin.IN)

while True:
    # check whether the button is clicked
    while btn.value() == 0:
        # blink the LED
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
    # reset the LED
    led.value(0)
