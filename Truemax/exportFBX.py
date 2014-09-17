# Author: Sofia Elena Jakobsen Manioudakis
# Version: 1.0
# Export script for Unity Game models
import maya.cmds as cmds
import maya.mel as mel
import os


def export_asset():
    scene_file_raw = str(cmds.file(q=1, sceneName=1))
    file_dir = os.path.dirname(scene_file_raw)
    file_name = os.path.basename(os.path.splitext(scene_file_raw)[0])
    export_dir = os.path.join(file_dir, "export")

    if not os.path.exists(export_dir):
        os.mkdir(export_dir)

    scene_fbx = os.path.join(export_dir, file_name + ".fbx")
    assets = cmds.ls(sl=1)
    len(assets)
    if len(assets) == 0:
        print ">>>>> Please select geometry <<<<<"
    else:
        # Not pretty but there is not exporting allowed in Python...
        preset_file = "{0}{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep,
                                         "UnityExport.fbxexportpreset").replace("\\", "/")
        mel.eval('FBXLoadExportPresetFile -f "{0}";'.format(preset_file))
        mel.eval('FBXExport -f "{0}" -s;'.format(scene_fbx.replace("\\", "/")))