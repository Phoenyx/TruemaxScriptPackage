
from pymel.all import *
import maya.cmds as cmds


def name_compare():
    # First selection (incorrect naming)
    cmds.select(cl=1)
    cmds.select(allDagObjects=1)
    # Select everything under the dagObject.
    cmds.select(hi=1)
    # Deselect the shapes
    cmds.select("*Shape*", deselect=1)
    #The selection now equals the objects in the scene
    select_all = cmds.ls(sl=1)

    # Second selection(correct naming)
    # TRY EXCEPT !!?!?! DAN DAN DAN. FAILS IF TOP NODE NAME ISNT CORRECT: CANT MATCH THE TWO...
    scene_file_raw = str(cmds.file(q=1, sceneName=1, shortName=1))
    topNode = str(mel.match("[a*-z]+[A-Z]", scene_file_raw))

    select_geo = []

    cmds.select(cl=1)
    if cmds.objExists(topNode):
        cmds.select(topNode)

        if cmds.objExists("*_geo"):
            cmds.select("*_geo", add=1)
            select_geo = cmds.ls(sl=1)
        else:
            select_geo = cmds.ls(sl=1)

    else:
        select_geo = []


    if (len(select_geo) == len(select_all)):
        return True
    else:
        return False