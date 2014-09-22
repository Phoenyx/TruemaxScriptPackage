__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds
from pymel.all import mel
from hfFixShading import hfFixBadShading

class ModuleOther(manager.Module):

    def create_ui(self):
        tab=str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True,label="Helpers")
        cmds.columnLayout()
        cmds.button(command=lambda *args: hfFixBadShading(),label="Fix Face Assignments on Scene Objects")
        cmds.button(command=lambda *args: mel.jh_findDuplicateNames(),label="Find Duplicate Names")
        cmds.button(command=lambda *args: mel.cometRename(),label="Rename Multiple Objects")
        cmds.button(command=lambda *args: mel.fixRenderLayerOutAdjustmentErrors(),label="Fix Render Layer Errors")
        cmds.button(command=lambda *args: mel.thmbnailUpdTgl(),label="Render Thumbnail Update Toggle")
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.frameLayout(collapsable=True,label="Scripting")
        cmds.columnLayout()
        cmds.button(command=lambda *args: mel.melomatic(),label="Mel-O-Matic")
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Other"

def initModule(manager):
    return ModuleOther(manager)