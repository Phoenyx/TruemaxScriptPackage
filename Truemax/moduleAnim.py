from Truemax import paie
from Truemax.moduleScene import get_author_initials

__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds
from pymel.all import mel
import external.poseLibModule as pose

if get_author_initials() == 'mj':
    bg_colour = [0.9, 0.4, 1]
else:
    bg_colour = [0.4, 0.4, 0.4]


class ModuleAnim(manager.Module):
    def hierarchy_selection(self):

        cmds.select(hi=True)

        sel = cmds.ls(sl=True)
        selCtrl = []

        for obj in sel:
            checkCtrl = "_ctrl" in obj + ".name"
            checkCtrlU = "_ctrl_" in obj + ".name"
            chechShape = "Shape" in obj + ".name"
            checkZero = "zero" in obj + ".name"
            checkGrp = "grp" in obj + ".name"
            checkHandel = "Handle" in obj + ".name"
            if checkCtrl == True and chechShape == False and checkZero == False and checkGrp == False and checkCtrlU == False and checkHandel == False and mc.objectType(
                    obj, i="cluster") == False:
                selCtrl.append(obj)

        if len(selCtrl) != 0:
            cmds.select(selCtrl, r=True)

    def create_ui(self):
        tab = str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True, label="Common")
        cmds.columnLayout()
        cmds.button(command=lambda *args: mel.autoTangent(), label="autoTangent", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: self.hierarchy_selection(), label="HierarchySelection",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.tweenMachine(), label="TweenMachine", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.zoomerator(), label="Zoomerator", backgroundColor=bg_colour)
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.frameLayout(collapsable=True, label="Import/Export")
        cmds.columnLayout()
        cmds.button(command=lambda *args: mel.dkAnim(), label="dkAnim", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: paie.GUI(), label="paie", backgroundColor=bg_colour)
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Anim"


def initModule(manager):
    return ModuleAnim(manager)