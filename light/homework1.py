import spidev
import time
import sys, pygame


delay = 2
ldr_channel = 0
pygame.init()


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
    if ldr_value >= 424 and ldr_value <= 428:
        pygame.mixer.music.load("sol.wav")
        pygame.mixer.music.play(1)
    else if ldr_value >= 456 and ldr_value <= 463:
        pygame.mixer.music.load("la.wav")
        pygame.mixer.music.play(1)
    else if ldr_value >= 438 and ldr_value <= 440:
        pygame.mixer.music.load("si.wav")
        pygame.mixer.music.play(1)
    else if ldr_value >= 383 and ldr_value <= 387:
        pygame.mixer.music.load("fa.wav")
        pygame.mixer.music.play(1)
    else if ldr_value >= 338 and ldr_value <= 342:
        pygame.mixer.music.load("mi.wav")
        pygame.mixer.music.play(1)
    else if ldr_value >= 371 and ldr_value <= 377:
        pygame.mixer.music.load("re.wav")
        pygame.mixer.music.play(1)
    else if ldr_value >= 395 and ldr_value <= 422:
        pygame.mixer.music.load("sol.wav")
        pygame.mixer.music.play(1)

    time.sleep(delay)
