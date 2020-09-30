# CPX-IronMan-Repulsor
Circuit Playground Express (CPX) IronMan Repulsor effect

This project was born of my 3 year old’s consuming fascination with all things Marvel and particularly IronMan. In short, he wanted a ‘real’ IronMan blaster. Now without actually manufacturing some kind of energy weapon, I settled on the Circuit Playground Express as it has a ring of LED’s and a speaker that should do the job nicely.

After it arrived and I had finished playing with it, I got to work making the first prototype of the program using https://makecode.adafruit.com/. This drag and drop software is a great way to quickly and easily play around with the various functions of the CPX.

Once I had a fair idea of how I wanted this to work I set up the CPX to work with CircuitPython by following the instructions here https://learn.adafruit.com/using-edublocks-with-circuit-playground-express/connecting-to-the-cpx.
 
I wrote my program in the MU editor (https://codewith.mu/) before copying it over to VSCode (https://code.visualstudio.com/) to make use of the deeper functionality such as the intelligent code completion and GIT, although the MU editor was a pleasure to use with the CPX.

Next, I had to create a .wav file for the CPX to use as part of its routine. This was done by using Audacity (https://www.audacityteam.org/) to record a soundbite from a YouTube video, I’m not sure which one but any video with decent sound quality will work. Remember to save the sound file at 22050 Hz and in mono for it to work with the CPX. The actual .wav sound file I used can be found here https://github.com/SebastianBenson/CPX-IronMan-Repulsor.

Let’s walk through the actual code now.

All python scripts will begin by importing the relevant libraries that are needed to run the code. In this case we need to import ‘time’ in order to make use of the time.sleep method so as to fine tune the way our NeoPixels light up. The ‘from adafruit_circuitplayground.express import cpx’ line lets us work with all the various CPX functions such as the switch, buttons and NeoPixels.

Next, we are just saving the NeoPixel colours to their namesake variables for ease of use and set a value that we are comfortable with for the brightness. Note, the brightness can also be adjusted by changing the colour values themselves e.g. red = (25,0,0) is 10% as bright.
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
cpx.pixels.brightness = 0.1

Now we have our variables set, let’s start working on the actual control flow.

By beginning with a while loop, we can continuously check if a condition or set of conditions are met and then execute some action. In this case we are checking to see what position our switch is in (either on or off) and change the colour of our NeoPixels accordingly. 
 The other condition we are checking for is whether either: 
Button A is pressed, in which case the CPX fills all the NeoPixels blue or red depending on the switch position.
 
Button B is pressed, in which case all the NeoPixels turn off again. 
The CPX is shaken a sufficient amount to trigger the NeoPixels to light up one by one, play our sound effect, then turn off. 

The shake value begins at 10, meaning at-rest and ends at 30. So adjust your value to calibrate the sensitivity to your liking.
