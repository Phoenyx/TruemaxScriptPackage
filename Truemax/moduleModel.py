from Truemax.moduleScene import get_author_initials

__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds
from pymel.all import mel
from reverseNormals import reverseNormals

if get_author_initials()=='mj':
    bg_colour=[0.9, 0.3, 0.5]
else:
    bg_colour=[0.4,0.4,0.4]

class ModuleModel(manager.Module):

    def __init__(self, mngr):
        manager.Module.__init__(self, mngr)

    def create_ui(self):
        tab = str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True, label="Common")
        cmds.columnLayout()
        cmds.button(command=lambda *args: mel.FBImgpln(), label="Create Image Plane", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.FBpolyPlanarize(), label="Poly Planarize", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.ToggleFaceNormalDisplay(), label="Show Face Normals on Selected", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: reverseNormals(), label="Reverse Normals on Selected", backgroundColor=bg_colour)
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Model"

def initModule(manager):
    return ModuleModel(manager)