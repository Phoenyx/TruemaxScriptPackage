__author__ = 'sofiaelm'


# Script that deletes all display layers in the scene
# Skips the invisible default display layer

from pymel.all import *


def deleteDPLayers():
    layers = ls(type="displayLayer")
    for layer in layers:
        if layer == "defaultLayer":
            pass

        else:
            print "deleted "+layer
            delete(layer)
