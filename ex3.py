from machine import I2C, Pin
import time

class MCP9808:
    # resolution levels
    RES_LEVEL1 = b'\x00' # +0.5C
    RES_LEVEL2 = b'\x01' # +0.25C
    RES_LEVEL3 = b'\x10' # +0.125C
    RES_LEVEL4 = b'\x11' # +0.0625C

    def __init__ (self, scl, sda):
        self._i2c = I2C(scl=scl, sda=sda)
        self._addr = 0x18
        self._temp_reg = 0x05
        self._res_reg = 0x08

    def _temp_to_c (self, raw_data):
        val = raw_data[0] << 8 | raw_data[1]
        temp = (val & 0xFFF) / 16
        if val & 0x1000:
            temp -= 256
        return temp

    def read_temperature (self):
        data = self._i2c.readfrom_mem(self._addr, self._temp_reg, 2)
        return self._temp_to_c(data)

    def set_resolution_level (self, level):
        self._i2c.writeto_mem(self._addr, self._res_reg, level)

# initial state
currentLED = "GREEN"

# setup button and the LEDs
mcp = MCP9808(scl=Pin(22), sda=Pin(23))
mcp.set_resolution_level(MCP9808.RES_LEVEL1)
leds = {"GREEN": Pin(15, Pin.OUT), "YELLOW": Pin(32, Pin.OUT), "RED": Pin(13, Pin.OUT)}

while True:
    # read temperature
    temp = mcp.read_temperature()

    # decide on the temperature level
    if temp > 31:
        currentLED = "RED"
    elif temp > 29:
        currentLED = "YELLOW"
    else:
        currentLED = "GREEN"

    # clear all LEDs
    for l in leds:
        leds[l].value(0)
        
    # set current LED
    leds[currentLED].value(1)
    time.sleep(0.01)
