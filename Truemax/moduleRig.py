from Truemax.moduleScene import get_author_initials

__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds
from pymel.all import mel

if get_author_initials() == 'mj':
    bg_colour = [0.9, 0.4, 1]
else:
    bg_colour = [0.4, 0.4, 0.4]


class ModuleRig(manager.Module):
    def create_ui(self):
        tab = str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True, label="Common")
        cmds.columnLayout()
        cmds.button(command=lambda *args: mel.abAutoRig(), label="AB Auto Rig", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.rbSetLocalPivot(), label="Set Geo Pivot To Sel",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.joint_at_pivot(), label="Joint at Pivot", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.JointTool(), label="Joint Tool", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.rbZeroTransformer("_zero"), label="Zero Out Joint",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.IKHandleTool(), label="IK Handle Tool", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.scMoveJntsModeOnOff(1), label="Move Joints On", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.scMoveJntsModeOnOff(0), label="Move Joints Off",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.rb_ShapesWindow(), label="Controller Shapes", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.wp_shapeParent(), label="Parent Shape", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.ArtPaintSkinWeightsTool(), label="Maya Paint Skin Weights",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.paintSkinWeights(), label="Vertex Paint Skin Weights",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.cometSaveWeights(), label="-Comet- Save Skin Weights",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.objectColorPalette(), label="Wireframe Colour", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.lockNonKeyable_all(), label="Lock and make Non-keyable (Selected)",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.NodeEditorWindow(), label="Node Editor", backgroundColor=bg_colour)
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Rig"


def initModule(manager):
    return ModuleRig(manager)