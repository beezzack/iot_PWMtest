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
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

while True:
    ldr_value = readadc(ldr_channel)
    print("-----------------------------------")
    print("LDR Value: %d" % ldr_value)
    if ldr_value >= 455 and ldr_value <= 465:
        pygame.mixer.music.load("la.wav")
        pygame.mixer.music.play(1)
    elif ldr_value >= 435 and ldr_value <= 445:
        pygame.mixer.music.load("si.wav")
        pygame.mixer.music.play(1)
    elif ldr_value >= 410 and ldr_value <= 420:
        pygame.mixer.music.load("sol.wav")
        pygame.mixer.music.play(1)
    elif ldr_value >= 385 and ldr_value <= 390:
        pygame.mixer.music.load("fa.wav")
        pygame.mixer.music.play(1)
    elif ldr_value >= 315 and ldr_value <= 340:
        pygame.mixer.music.load("mi.wav")
        pygame.mixer.music.play(1)
    elif ldr_value >= 345 and ldr_value < 380:
        pygame.mixer.music.load("re.wav")
        pygame.mixer.music.play(1)
    elif ldr_value >= 425 and ldr_value <= 435:
        pygame.mixer.music.load("do.wav")
        pygame.mixer.music.play(1)    

    time.sleep(delay)
