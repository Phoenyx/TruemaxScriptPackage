
from hfFixShading import hfCheckShading
import hfFixShading as hfFS
import maya.cmds as cmds


def checkList():
    if hfFS.hfCheckShading():
        print "face assignment detected"
    else:
        print "No face assignment"