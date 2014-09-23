__author__ = 'sofiaelm'

from pymel.all import *


def detect_history():
    scene_file_raw = str(cmds.file(q=1, sceneName=1, shortName=1))
    topNode = str(mel.match("[a*-z]+[A-Z]", scene_file_raw))

    select(topNode)
    select(hi=1)
    select("*Shape*", deselect=1)
    select(topNode, deselect=1)
    objects = cmds.ls(sl=1)

    for obj in objects:
        history = cmds.listHistory(obj)
        if len(history) > 1:
            return False

    return True