import time
from adafruit_circuitplayground.express import cpx
blue = (0,0,255)
black = (0,0,0)
while True:
    if cpx.button_a:
        cpx.pixels.fill((black))
        cpx.pixels.show()
    if cpx.shake(20):
        for n in range(0,10):
            cpx.pixels[n]=blue
            time.sleep(0.1)
        cpx.play_file('repulsor.wav')
        time.sleep(1)
        cpx.pixels.fill((black))
        