import os

__author__ = 'sofiaelm'
import manager
import maya.cmds as cmds
from pymel.all import mel


class ModuleScene(manager.Module):

    cleanScene = "cleanScene"

    def __init__(self, mngr):
        manager.Module.__init__(self, mngr)

    def new_scene(self):
        window = None

        def new_scene_click(*args):
            cmds.SaveSceneAs()
            if cmds.window(window, exists=True):
                cmds.deleteUI(window, window=True)

        cmds.file(newFile=True, force=True)
        location = "{0}{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep, self.cleanScene)
        self.set_project(location)
        cmds.file("cleanScene.mb", open=True)
        cmds.file(renameToSave=True)
        window = cmds.window(title="Oi!", widthHeight=(250, 100))
        cmds.columnLayout(adjustableColumn=True)
        cmds.frameLayout(label='Please save your scene!')
        cmds.button(label='Ofcourse!', command=new_scene_click)
        cmds.setParent('..')
        cmds.showWindow(window)

    def set_project(self, location):
        mel.setProject(location)

    def create_ui(self):

        def setProjectAsCurrDirectory():
            filePath = cmds.file(query =True, expandName=True)
            directory = os.path.dirname(filePath)
            self.set_project(directory)

        tab = str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True, label="Common")
        cmds.columnLayout()
        cmds.button(command=lambda *args: self.new_scene(), label="New Work Scene")
        cmds.button(command=lambda *args: setProjectAsCurrDirectory(), label="Set Project")
        cmds.button(command=lambda *args: mel.deleteUnusedNodes(), label="Delete Unused Nodes")
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Scene"


def initModule(manager):
    return ModuleScene(manager)