# Author: Sofia Elena Jakobsen Manioudakis
# Version: 1.0
# Export script for Unity Game models

import sys
from pymel.all import *
from Truemax.checkNaming import get_top_node


def export_asset():
    continueDialog = cmds.confirmDialog(title='Make Model FBX',
                                        message='Are you sure your model is ready to be exported?',
                                        button=['Model', 'Animation', 'No'], cancelButton='No', defaultButton='No',
                                        dismissString='No')
    if continueDialog == "Model":
        top_node = get_top_node()
        file_dir = os.path.dirname(cmds.file(q=1, sceneName=1))
        export_dir = os.path.join(os.path.dirname(file_dir), "export")

        if not os.path.exists(export_dir):
            os.mkdir(export_dir)

        scene_fbx = os.path.join(export_dir, str(top_node) + ".fbx")

        if cmds.objExists(str(top_node)) == 0:
            cmds.warning(">>>>> Top node named incorrectly or non-existent <<<<<")

        else:
            cmds.select(top_node)
            # Not pretty but there is not exporting allowed in Python...
            preset_file = "{0}{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep,
                                             "UnityExport.fbxexportpreset").replace("\\", "/")
            mel.eval('FBXLoadExportPresetFile -f "{0}";'.format(preset_file))
            mel.eval('FBXExport -f "{0}" -s;'.format(scene_fbx.replace("\\", "/")))
            sys.stdout.write(">>>>> FBX Model Exported! <<<<<")

    if continueDialog == "Animation":
        top_node = get_top_node()
        file_dir = os.path.dirname(cmds.file(q=1, sceneName=1))
        export_dir = os.path.join(os.path.dirname(file_dir), "export")

        if not os.path.exists(export_dir):
            os.mkdir(export_dir)

        scene_fbx = os.path.join(export_dir, str(top_node) + "ANIM" + ".fbx")

        if cmds.objExists("geo_grp") == 0:
            cmds.warning(">>>>> No group matches name 'geo_grp' <<<<<")

        else:
            cmds.select("geo_grp")
            # Not pretty but there is not exporting allowed in Python...
            preset_file = "{0}{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep,
                                             "UnityExport.fbxexportpreset").replace("\\", "/")
            mel.eval('FBXLoadExportPresetFile -f "{0}";'.format(preset_file))
            mel.eval('FBXExport -f "{0}" -s;'.format(scene_fbx.replace("\\", "/")))
            sys.stdout.write(">>>>> FBX with Animation Exported! <<<<<")