import time
from adafruit_circuitplayground.express import cpx
#This is just a nice way to store our colour values in an easy to read/use way.
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
#The value for cpx.pixels.brightness can be any value from 0.00 - 1.00, with 1.00 being the brightest.
cpx.pixels.brightness = 0.1
#This is the start of our control flow. If the switch is off, our cpx board will use it's blue lights or the red lights, if the switch is on.
while True:
    if cpx.switch:
        cpx.red_led = False
        #This code instructs the cpx board to assign the blue colour to the NeoPixels, and turn them on if the 'a' button is pressed.
        if cpx.button_a:
            cpx.pixels.fill((blue))
            cpx.pixels.show()
        #When we press the 'b' button, all our NeoPixels turn off.
        if cpx.button_b:
            cpx.pixels.fill((black))
            cpx.pixels.show()
        #When the CPX feels a shake it runs the following code block, which lights up the ring incrementally while playing the Repulsor.wav sound file before turning all the NeoPixels off again.
        if cpx.shake(15):#The shake value adjusts the sensitivity, with 10 being at-rest and 30 being the hardest to register.
            for n in range(0,10):
                cpx.pixels[n]=blue
                time.sleep(0.1)
            cpx.play_file('repulsor.wav')
            time.sleep(1)
            cpx.pixels.fill((black))
    #The code here is a mirror of the code above, just with a twist to the dark side ;)
    else:
        cpx.red_led = True
        if cpx.button_a:
            cpx.pixels.fill((red))
            cpx.pixels.show()
        if cpx.button_b:
            cpx.pixels.fill((black))
            cpx.pixels.show()
        if cpx.shake(15):
            for n in range(0,10):
                cpx.pixels[n]=red
                time.sleep(0.1)
            cpx.play_file('repulsor.wav')
            time.sleep(1)
            cpx.pixels.fill((black))
