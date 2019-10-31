from machine import Pin
import time

# initial state
currentLED = "GREEN"

# setup button and the LEDs
btn = Pin(14, Pin.IN)
leds = {"GREEN": Pin(15, Pin.OUT), "YELLOW": Pin(32, Pin.OUT), "RED": Pin(13, Pin.OUT)}

# set the LED to the initial value
leds[currentLED].value(1)

while True:
    if btn.value() == 0:
        # debounce the button for 10ms
        time.sleep(0.01)
        # switch the LED
        if currentLED == "GREEN":
            currentLED = "YELLOW"
        elif currentLED == "YELLOW":
            currentLED = "RED"
        elif currentLED == "RED":
            currentLED = "GREEN"
        else:
            pass
        # clear all LEDs
        for l in leds:
            leds[l].value(0)
        # set current LED
        leds[currentLED].value(1)
        # wait for the button to be released
        while btn.value() == 0:
            pass
    time.sleep(0.01)
