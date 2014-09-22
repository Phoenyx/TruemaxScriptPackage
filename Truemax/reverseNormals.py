from pymel.all import *
import sys

def reverseNormals():

    def mPrint(message):
        sys.stdout.write(message + '\n')

    assets=ls(sl=1)
    amount=len(assets)

    message=("Reversed normals on "+str(amount)+" objects")
    
    i=0
    while (i < amount):
        polyNormal(assets[i],ch=1,userNormalMode=0,normalMode=0)
        i=i+1
        
    mPrint(message)

