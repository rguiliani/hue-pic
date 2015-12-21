#!/usr/bin/env python
from phue import Bridge
from pprint import pprint
from rgb_cie import Converter #https://github.com/benknight/hue-python-rgb-converter/blob/master/rgb_cie.py
import math
from PIL import Image
import colorsys
import time
import numpy
import json

b = Bridge('192.168.0.2')

image = Image.open('test2.jpg')
width, height = image.size
image = image.load()

#b.connect()
lights = b.lights
    
def get_hue(pixel):
    converter = Converter()
    converter.rgbToCIE1931(pixel[0], pixel[1], pixel[2])
    return converter.getCIEColor()

def get_brightness(pixel):
    r, g, b = pixel
    return (r + g + b) / 3

def change_lights(value, brightness, lights):
    for i in lights:
        i.xy = value
        #i.saturation = 120
        i.brightness = brightness
   
def setup_lights(lights):
    for i in lights:
        i.on = True
        i.saturation = 255
        i.transitiontime = 4
 
setup_lights(lights)

for y in xrange(0,height):
    for x in xrange(0,width):
        pixel = image[x,y]
        value = get_hue(pixel)
        brightness = get_brightness(pixel)
        print value
        change_lights(value, brightness, lights)
        time.sleep(.75)
