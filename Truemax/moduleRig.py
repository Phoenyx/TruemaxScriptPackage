__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds
from pymel.all import mel

class ModuleRig(manager.Module):

    def create_ui(self):
        tab = str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True, label="Common")
        cmds.columnLayout()
        cmds.button(command=lambda *args: mel.rbSetLocalPivot(), label="Set Geo Pivot To Sel")
        cmds.button(command=lambda *args: mel.joint_at_pivot(), label="Joint at Pivot")
        cmds.button(command=lambda *args: mel.JointTool(), label="Joint Tool")
        cmds.button(command=lambda *args: mel.IKHandleTool(), label="IK Handle Tool")
        cmds.button(command=lambda *args: mel.wp_shapeParent(), label="Parent Shape")
        cmds.button(command=lambda *args: mel.paintSkinWeights(), label="Paint Skin Weights")
        cmds.button(command=lambda *args: mel.objectColorPalette(), label="Wireframe Colour")
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Rig"

def initModule(manager):
    return ModuleRig(manager)