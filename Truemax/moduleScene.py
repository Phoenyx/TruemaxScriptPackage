from Truemax.checkNaming import get_top_node
from Truemax.hfFixShading import hfFixBadShading

__author__ = 'sofiaelm'
import os
import Truemax.exportFBX as exportFBX
from Truemax import checkList
import manager
import maya.cmds as cmds
from pymel.all import mel
import pymel.core as pm
from pymel.all import *

# Reloads script when update is ran
reload(exportFBX)
reload(checkList)

SCENE_FOLDER = "scenes"
TURNTABLE_FOLDER = "turnTable"
EXPORT_FOLDER = "export"
SOURCEIMAGES_FOLDER = "sourceimages"


# Gets first and last letter of username
def get_author_initials():
    user = os.getenv('user', "na")
    return str(user[0] + user[-1]).lower()


class ModuleScene(manager.Module):
    cleanScene = "cleanScene"

    def __init__(self, mngr):
        manager.Module.__init__(self, mngr)

        self.statusDir = None

        if "assetslocation" in mngr.config:
            self.statusDir = mngr.config["assetslocation"]

        # Reset check status on selection
        cmds.scriptJob(event=["DagObjectCreated", lambda *args: self.reset_check_list()], protected=True)

    def new_scene(self):

        cmds.file(newFile=True, force=True)
        location = "{0}{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep, self.cleanScene)
        self.set_project(location)
        cmds.file("cleanScene.ma", open=True)

        select_dir = pm.fileDialog2(fileMode=2, dialogStyle=3, startingDirectory=self.statusDir)

        if select_dir != None:
            print select_dir[0]
            sDir = str(select_dir[0])

            result = cmds.promptDialog(
                title='Asset Name',
                message='Enter Name:',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

            if result == 'OK':
                assetName = cmds.promptDialog(query=True, text=True)
            print assetName

            # makes project folder
            projectFolder = os.path.join(sDir, assetName)
            if not os.path.exists(projectFolder):
                print "Creating {0}".format(projectFolder)
                os.makedirs(projectFolder)

            # makes scenes folder
            scenesFolder = os.path.join(projectFolder, SCENE_FOLDER)
            if not os.path.exists(scenesFolder):
                print "Creating {0}".format(scenesFolder)
                os.makedirs(scenesFolder)

                # makes turntable folder
            turntableFolder = os.path.join(projectFolder, TURNTABLE_FOLDER)
            if not os.path.exists(turntableFolder):
                print "Creating {0}".format(turntableFolder)
                os.makedirs(turntableFolder)

                # makes export folder
            exportFolder = os.path.join(projectFolder, EXPORT_FOLDER)
            if not os.path.exists(exportFolder):
                print "Creating {0}".format(exportFolder)
                os.makedirs(exportFolder)

            # makes sourceimages folder
            sourceimagesFolder = os.path.join(projectFolder, SOURCEIMAGES_FOLDER)
            if not os.path.exists(sourceimagesFolder):
                print "Creating {0}".format(sourceimagesFolder)
                os.makedirs(sourceimagesFolder)

            fileName = assetName + "_v001_" + get_author_initials() + ".ma"
            fileSavePath = os.path.join(scenesFolder, fileName)
            print fileSavePath
            cmds.file(rename=fileSavePath)
            cmds.file(save=True)

            self.setProjectAsCurrDirectory()
            cmds.currentUnit(linear='m')

            if cmds.pluginInfo('fbxmaya', query=True, loaded=True) == False:
                cmds.loadPlugin('fbxmaya', quiet=True)
                cmds.pluginInfo('fbxmaya', edit=True, autoload=True)

    def set_project(self, location):
        mel.setProject(location)

    def setProjectAsCurrDirectory(self):
        filePath = cmds.file(query=True, expandName=True)
        directory = os.path.dirname(filePath)
        project = os.path.dirname(directory)
        self.set_project(project)

    def importRefCube(self):
        location = "{0}{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep, self.cleanScene)
        self.set_project(location)
        cmds.file("refCube.ma", i=True)
        self.setProjectAsCurrDirectory()

    def update_check_list(self):
        check_output = checkList.check_list()
        output_errors = "\n".join(check_output[1])

        if check_output[0]:
            cmds.text(self.statusText, label=output_errors, edit=True, backgroundColor=[0, 1, 0])
        else:
            cmds.text(self.statusText, label=output_errors, edit=True, backgroundColor=[1, 0, 0])

    def reset_check_list(self):
        cmds.text(self.statusText, edit=True, backgroundColor=[1, 1, 0])

    def select_hierachy(self):
        cmds.select(hi=1)

    def select_top_node(self):
        cmds.select(get_top_node())

    def pivot_at_origin(self):
        self.select_top_node()
        xform(zeroTransformPivots=1)

    def create_ui(self):
        if get_author_initials() == 'mj':
            bg_colour = [0.9, 0.3, 0.6]
        else:
            bg_colour = [0.4, 0.4, 0.4]

        tab = str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.frameLayout(collapsable=True, label="Common")
        cmds.columnLayout()
        cmds.button(command=lambda *args: self.new_scene(), label="New Work Scene", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: self.setProjectAsCurrDirectory(), label="Set Project",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: self.importRefCube(), label="Import Reference Cube",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.reset(), label="Create Playblast Turntable", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.deleteUnusedNodes(), label="Delete Unused Nodes",
                    backgroundColor=bg_colour)
        cmds.button(command=lambda *args: exportFBX.export_asset(), label="Export in FBX", backgroundColor=bg_colour)
        cmds.setParent('..')
        cmds.setParent('..')

        cmds.frameLayout(collapsable=True, label="Status")
        cmds.columnLayout(rowSpacing=2)
        cmds.button(command=lambda *args: self.update_check_list(), label="Update Status", backgroundColor=bg_colour)
        cmds.text(label="Status errors:", align="left", backgroundColor=[0.2, 0.2, 0.2], height=15)
        self.statusText = cmds.text("Status", backgroundColor=[1, 1, 0])
        self.statusText = cmds.text(self.statusText, query=True, fullPathName=True)

        cmds.setParent('..')
        cmds.setParent('..')
        cmds.frameLayout(collapsable=True, label="Check List")
        cmds.columnLayout(rowSpacing=2)
        cmds.button(command=lambda *args: hfFixBadShading(),label="Fix Face Assignments on Scene Objects", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: self.select_top_node(),  label="Select Top Node", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: self.select_hierachy(),  label="Select Hierachy", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.FreezeTransformations(), label="Freeze Transformations", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: mel.DeleteHistory(), label="Delete History", backgroundColor=bg_colour)
        cmds.button(command=lambda *args: self.pivot_at_origin(), label="Pivot at Origin", backgroundColor=bg_colour)
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        return tab, "Scene"


def initModule(manager):
    return ModuleScene(manager)