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

