import spidev
import time


delay = 2
ldr_channel = 0


spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def readadc(adcnum):
    if adcnum >7 or adcnum <0:
        return -1
    r = spi.xder2([1, 8 + adcum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

while True:
    ldr_value = readadc(ldr_channel)
    print("-----------------------------------")
    print("LDR Value: %d" % ldr_value)
    time.sleep(delay)
    
