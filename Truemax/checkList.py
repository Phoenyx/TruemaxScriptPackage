from Truemax import checkTransforms
import Truemax.checkNaming as checkNaming
import Truemax.detectHistory as detectHistory
import Truemax.checkPivot as checkPivot
from hfFixShading import hfCheckShading
import sys
import maya.cmds as cmds

reload(checkNaming)
reload(checkTransforms)
reload(detectHistory)

def top_node_count():
    cmds.select(allDagObjects=1)
    all_top_nodes = cmds.ls(sl=1)

    if len(all_top_nodes) > 1:
        cmds.warning("You have more than one top node!")
        return False

def check_list():

    checklist = [
        {"status": top_node_count(), "error": "More than one top node!"},
        {"status": checkNaming.name_compare(), "error": "Objects have incorrect naming"},
        {"status": checkTransforms.check_transforms(), "error": "Objects have non zero transforms!"},
        {"status": checkPivot.check_pivot(), "error": "Pivot not at Origin!"},
        {"status": hfCheckShading() is False, "error": "Face assignment detected!"},
        {"status": detectHistory.detect_history(), "error": "Objects have construction history/face assignment"},
    ]

    errors = []
    for c in checklist:
        if c["status"] is False:
            errors.append(c["error"])


    if len(errors):
        return False, errors
    else:
        sys.stdout.write("Object(s) checked. All is well, yay!\n")
        return True, ["All Perfect"]