from Truemax import checkTransforms
import Truemax.checkNaming as checkNaming
import Truemax.detectHistory as detectHistory
from Truemax.checkTransforms import check_transforms
import Truemax.checkTransforms as check_transforms
from Truemax.detectHistory import detect_history
from hfFixShading import hfCheckShading
import maya.cmds as cmds
import sys


reload(checkNaming)
reload(checkTransforms)
reload(detectHistory)


def check_list():
    if not checkTransforms.check_transforms() or hfCheckShading() or not detectHistory.detect_history() or not checkNaming.name_compare():
        cmds.warning("Found problems! See Script Editor for more details")
        return False
    else:
        sys.stdout.write("Object(s) checked. All is well, yay!\n")
        return True