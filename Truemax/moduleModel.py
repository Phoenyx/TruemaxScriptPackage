__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds
from pymel.all import mel
from external import spPaint3dGui

class ModuleModel(manager.Module):

    def __init__(self, mngr):
        manager.Module.__init__(mngr)

        self.spPaint3dwin = spPaint3dGui.spPaint3dWin()

    def create_ui(self):
        tab = str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True, label="Common")
        cmds.columnLayout()
        cmds.button()
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Model"

def initModule(manager):
    return ModuleModel(manager)