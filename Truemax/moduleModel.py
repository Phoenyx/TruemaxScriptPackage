__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds
from pymel.all import mel
from reverseNormals import reverseNormals

class ModuleModel(manager.Module):

    def __init__(self, mngr):
        manager.Module.__init__(self, mngr)


    def select_hierachy(self):
        cmds.select(hi=1)

    def create_ui(self):
        tab = str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True, label="Common")
        cmds.columnLayout()
        cmds.button(command=lambda *args: mel.FBImgpln(), label="Create Image Plane")
        cmds.button(command=lambda *args: mel.FBpolyPlanarize(), label="Poly Planarize")
        cmds.button(command=lambda *args: self.select_hierachy(),  label="Select Hierachy")
        cmds.button(command=lambda *args: mel.FreezeTransformations(), label="Freeze Transformations")
        cmds.button(command=lambda *args: mel.DeleteHistory(), label="Delete History")
        cmds.button(command=lambda *args: mel.CenterPivot(), label="Center Pivot")
        cmds.button(command=lambda *args: mel.ToggleFaceNormalDisplay(), label="Show Face Normals on Selected")
        cmds.button(command=lambda *args: reverseNormals(), label="Reverse Normals on Selected")
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Model"

def initModule(manager):
    return ModuleModel(manager)