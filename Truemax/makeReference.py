from Truemax.checkNaming import get_top_node

__author__ = 'sofiaelm'

# Makes a reference file. Copies the current file and saves it in the "export" folder in the project directory.

import shutil
from pymel.all import *

REF_FOLDER = "export"
SCENE_FOLDER = "scenes"

def make_reference():

    def messageBox(msg):
        cmds.confirmDialog(title='Ref Script Response', message=msg, button=['OK'])
        sys.stdout.write(msg)

    def moveToReference(filePath):
        top_node = get_top_node()

        scene_file = top_node
        file_dir = os.path.dirname(cmds.file(q=1, sceneName=1))
        export_dir = os.path.join(os.path.dirname(file_dir), "export")

        if not os.path.exists(export_dir):
            os.mkdir(export_dir)

        try:
            if "export" not in filePath and "scenes" not in filePath:
                print "Folder structure incorrect"
                return False
            filename = top_node

            if top_node is not None:
                filepath = cmds.file(query=True, sceneName=True)
                newFile = os.path.join(export_dir, scene_file + "_REF.ma")
                messageBox("Copying {0} to {1}".format(filename, newFile))
                shutil.copy(filepath, newFile)
                return True
            else:
                messageBox("Naming convention is incorrect for {0}".format(filePath))
                return False
        except IOError:
            messageBox("Unable to copy file {0} to {1}".format(filename, newFile))
            return False

    filepath = cmds.file(query=True, sceneName=True)
    continueDialog = cmds.confirmDialog(title='Make Reference',
                                        message='Are you sure your model is ready to be referenced?',
                                        button=['Yes', 'No'], cancelButton='No', defaultButton='Yes', dismissString='No')
    if continueDialog == "Yes":
        cmds.file(save=True, type='mayaAscii')
        moveToReference(filepath)
        messageBox("\nReference Made!")
