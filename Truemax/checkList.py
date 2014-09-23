import Truemax.checkNaming as checkNaming
from Truemax.checkTransforms import check_transforms
from Truemax.detectHistory import detect_history
from hfFixShading import hfCheckShading

reload(checkNaming)


def check_list():
    if not check_transforms() or hfCheckShading() or not detect_history() or not checkNaming.name_compare():
        print "found problems!"
        return False
    else:
        print "No problems!"
        return True