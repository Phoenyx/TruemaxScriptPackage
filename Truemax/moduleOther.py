from Truemax.moduleScene import get_author_initials

__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds
from pymel.all import mel
from hfFixShading import hfFixBadShading

if get_author_initials()=='mj':
    bg_colour=[0.9, 0.3, 0.5]
else:
    bg_colour=[0.4,0.4,0.4]

class ModuleOther(manager.Module):

    def create_ui(self):


        tab=str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True,label="Helpers")
        cmds.columnLayout()
        cmds.button(command=lambda *args: mel.jh_findDuplicateNames(),label="Find Duplicate Names", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.cometRename(),label="Rename Multiple Objects", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.fixRenderLayerOutAdjustmentErrors(),label="Fix Render Layer Errors", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.thmbnailUpdTgl(),label="Render Thumbnail Update Toggle", backgroundColor=bg_colour)
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.frameLayout(collapsable=True,label="Scripting")
        cmds.columnLayout()
        cmds.button(command=lambda *args: mel.melomatic(),label="Mel-O-Matic", backgroundColor=bg_colour)
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Other"

def initModule(manager):
    return ModuleOther(manager)