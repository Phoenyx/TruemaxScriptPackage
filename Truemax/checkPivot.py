from Truemax.checkNaming import get_top_node

__author__ = 'sofiaelm'

# Checks if pivot for top node is set to 0,0,0 (origin)

from pymel.all import *

def check_pivot():
    origin = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    top_node=get_top_node()

    if xform(top_node,q=1,pivots=1) == origin:
        return True
    else:
        return False
