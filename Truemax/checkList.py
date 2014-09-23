from Truemax.checkNaming import name_compare
from Truemax.checkTransforms import check_transforms
from Truemax.detectHistory import detect_history
from hfFixShading import hfCheckShading


def checkList():
    if not check_transforms() or hfCheckShading() or not detect_history() or not name_compare():
        print "found problems!"
        return False
    else:
        print "No problems!"
        return True