__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds

class ModuleModel(manager.Module):

    def __init__(self, mngr):
        manager.Module.__init__(self, mngr)

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