__author__ = 'sofiaelm'
# version 1.0

"""
Before this script is run it is important to inform the animators that they must import the referenced character
and delete namespaces. They should also double check that their top node is named correctly
and that there is just one top node.
"""

from pymel.all import *
import maya.cmds as cmds

# Regex for our scene name structure. Example: genericTurnLeft45A_v013_sm
SCENE_FILE_NAME_REGEX = r'[a-zA-Z]+[0-9]+[A-Z]{1}_v[0-9]{3}_[a-zA-Z]{2}'

# Regex for our top node name structure. Example: genericTurnLeft45A
SCENE_FILE_TOP_NODE_REGEX = r'([a-zA-Z]+[0-9]+[A-Z]{1})(_)'


def exportAnimFBX():
    # Checks if the geometry group exists
    if cmds.objExists("geo_grp") == 0:
        cmds.warning(">>>>> No group matches name 'geo_grp' <<<<<")

    else:
        # if the export folder doesnt exist in the directory then create it.
        file_dir = os.path.dirname(cmds.file(q=1, sceneName=1))
        export_dir = os.path.join(os.path.dirname(file_dir), "export")
        if not os.path.exists(export_dir):
            os.mkdir(export_dir)

        # Get the full scene name
        scene_file_raw = str(cmds.file(q=1, sceneName=1, shortName=1))

        # See if the scene file is named correctly according to the regex
        if not re.match(SCENE_FILE_NAME_REGEX, scene_file_raw):
            print (">> Your scene file is named incorrectly <<")

        # See if the scene file is found in the top node Regex
        matches = re.search(SCENE_FILE_TOP_NODE_REGEX, scene_file_raw)
        if matches is None:
            print (">> Something went wrong... <<")

        # The regex consists of two groups: the name and the "_"
        groups = matches.groups()

        # Error if "groups" is too big
        if len(groups) != 2:
            print (">> Something went wrong... <<")

        # if the first element of "groups" is not in the scene, then error
        if groups[0] not in cmds.ls():
            print (">> Your top node is not named correctly <<")

        # the top node in the scene should be name like the first element of the group
        top_node = groups[0]

        # The name of the fbx we export is defined
        scene_fbx = os.path.join(export_dir, str(top_node) + ".fbx")

        # Get start time and end time of animation base on the timeline
        startTime = int(cmds.playbackOptions(query=True, minTime=True))
        endTime = int(cmds.playbackOptions(query=True, maxTime=True))

        print startTime
        print endTime

        # parent root ctrl to world
        cmds.parent('root_ctrl_zero', w=1)

        # select bind joints
        def selectBNDJNTS():
            cmds.select('R_shoulder_bnd_jnt', add=True)
            cmds.select('L_shoulder_bnd_jnt', add=True)
            cmds.select('R_knee_bnd_jnt', add=True)
            cmds.select('L_knee_bnd_jnt', add=True)
            cmds.select('neck_ctrl', add=True)

            cmds.select(hi=1, add=True)

            cmds.select('L_femur_bnd_jnt', add=True)
            cmds.select('R_femur_bnd_jnt', add=True)
            cmds.select('L_clavicle_ctrl', add=True)
            cmds.select('R_clavicle_ctrl', add=True)
            cmds.select('torso_ctrl', add=True)
            cmds.select('spine_01_ctrl', add=True)
            cmds.select('hip_ctrl', add=True)
            cmds.select('root_ctrl', add=True)

            # Deselect Palm, End joints and Shapes.
            cmds.select('*end_jnt*', d=1)
            cmds.select('*palm*', d=1)
            cmds.select('*Shape*', d=1)

        selectBNDJNTS()

        # Make a list of the selection
        selectBND = cmds.ls(sl=1)
        print selectBND

        # Bake anim to bind joints
        cmds.bakeResults(selectBND, t=(startTime, endTime))

        # Delete FK and IK joints+ctrls
        select(cl=1)
        cmds.select('*IK*', add=True)
        cmds.select('*FK*', add=True)
        cmds.select('*effector*', add=True)

        selectFKIK = cmds.ls(sl=1)
        cmds.delete(selectFKIK)

        # Select bind joints and geometry and export as FBX
        select(cl=1)
        selectBNDJNTS()
        cmds.select('*_geo', add=True)

        # Make a list of the selection to "Export selection" as FBX
        toExport = cmds.ls(sl=True)

        cmds.select(toExport)

        # Copied from another script. It is not pretty but exporting ia not allowed in Python
        # It exports the selection as FBX using a preset file. Writes message to command line when finished.
        preset_file = "{0}{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep,
                                         "UnityExport.fbxexportpreset").replace("\\", "/")
        mel.eval('FBXLoadExportPresetFile -f "{0}";'.format(preset_file))
        mel.eval('FBXExport -f "{0}" -s;'.format(scene_fbx.replace("\\", "/")))
        sys.stdout.write(">>>>> FBX with Animation Exported! <<<<<")
