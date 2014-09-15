__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds
from pymel.all import mel

class ModuleModel(manager.Module):

    def __init__(self, mngr):
        manager.Module.__init__(self, mngr)

    def create_ui(self):
        tab = str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True, label="Common")
        cmds.columnLayout()
        cmds.button(command=lambda *args: mel.FBImgpln(), label="Create Image Plane")
        cmds.button(command=lambda *args: mel.FBpolyPlanarize(), label="Poly Planarize")
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Model"

def initModule(manager):
    return ModuleModel(manager)