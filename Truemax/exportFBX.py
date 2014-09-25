# Author: Sofia Elena Jakobsen Manioudakis
# Version: 1.0
# Export script for Unity Game models
import maya.cmds as cmds
import maya.mel as mel
import os
from pymel.all import *


def export_asset():

    scene_file_raw=str(cmds.file(q=1,sceneName=1,shortName=1))
    scene_file=str(mel.match("[a*-z]+[A-Z]", scene_file_raw))
    file_dir = os.path.dirname(cmds.file(q=1,sceneName=1))
    export_dir = os.path.join(os.path.dirname(file_dir), "export")

    if not os.path.exists(export_dir):
        os.mkdir(export_dir)

    scene_fbx = os.path.join(export_dir, scene_file + ".fbx")
    assets = cmds.ls(sl=1)
    len(assets)
    if len(assets) == 0:
        cmds.warning( ">>>>> Please select geometry <<<<<")
    else:
        # Not pretty but there is not exporting allowed in Python...
        preset_file = "{0}{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep,
                                         "UnityExport.fbxexportpreset").replace("\\", "/")
        mel.eval('FBXLoadExportPresetFile -f "{0}";'.format(preset_file))
        mel.eval('FBXExport -f "{0}" -s;'.format(scene_fbx.replace("\\", "/")))