
from Truemax.detectHistory import detect_history
from hfFixShading import hfCheckShading
import hfFixShading as hfFS
import maya.cmds as cmds


def checkList():
    if hfFS.hfCheckShading():
        print "face assignment detected"
    if not check_transforms() or hfCheckShading() or not detect_history() or not name_compare():
    else:
        print "No face assignment"