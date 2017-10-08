#!/usr/bin/env python

from lifxlan import *

lifxlan = LifxLAN()

devices = lifxlan.get_lights()
bulb = devices[0]
print("Selected {}".format(bulb.get_label()))

bulb.set_brightness(20000)
