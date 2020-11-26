################ ANDROID AUTOMATION ###############
# Luis Combariza
# luis_combariza@outlook.com
# luisCombariza@linkedin.com


###################################################
# The following is a small script that Automates ##
# the game Stick hero using ppadb , PIL and numpy #
###################################################

from ppadb.client import Client
from PIL import Image
import numpy as numpy
import time as time


# Establish connection with android device
adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

# Check if no devices are connected to computer
if len(devices) == 0:
    print('No devices connected to the internet')

# choose first device
device = devices[0]

# program loop
while (True):
    # Take image currently on device screen
    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)

    # Open image and convert it to numpy array
    image = Image.open('screen.png')
    image = numpy.array(image, dtype=numpy.uint8)

    # Extract the pixel values that we will use to examine the game
    pixels = [list(i[:3]) for i in image[2000]]

    transitions = []
    ignore = True
    black = True

    # Iterate through the pixels and check their color
    for i, pixel in enumerate(pixels):
        r, g, b = [int(i) for i in pixel]
        print(r,g,b)

        if ignore and (r + g + b) != 0:
            continue

        ignore = False

        if black and (r + g + b) != 0:
            black = not black
            transitions.append(i)
            continue

        if not black and (r + g + b) == 0:
            black = not black
            transitions.append(i)
            continue

  