__author__ = 'sofiaelm'

# Import ref
# delete namespaces

from pymel.all import *
import maya.cmds as cmds

SCENE_FILE_TOP_NODE_REGEX = r'([a-zA-Z]+[0-9]+[A-Z]{1})(_)'

def exportAnimFBX():

    if cmds.objExists("geo_grp") == 0:
        cmds.warning(">>>>> No group matches name 'geo_grp' <<<<<")

    else:
        file_dir = os.path.dirname(cmds.file(q=1, sceneName=1))
        export_dir = os.path.join(os.path.dirname(file_dir), "export")
        if not os.path.exists(export_dir):
            os.mkdir(export_dir)

        scene_file_raw = str(cmds.file(q=1, sceneName=1, shortName=1))
        matches = re.search(SCENE_FILE_TOP_NODE_REGEX, scene_file_raw)
        if matches is None:
            print (">> Something went wrong... <<")

        groups = matches.groups()

        if len(groups) != 2:
            print (">> Something went wrong... <<")

        if groups[0] not in cmds.ls():
            print (">> Your top node is not named correctly <<")

        top_node = groups[0]
        scene_fbx = os.path.join(export_dir, str(top_node) + ".fbx")

        # Get start time and end time of anim
        startTime = int(cmds.playbackOptions(query=True, minTime=True))
        endTime = int(cmds.playbackOptions(query=True, maxTime=True))

        print startTime
        print endTime

        # parent root ctrl to world
        cmds.parent('root_ctrl_zero', w=1)

        # bake anim to bnd jnts
        # select bnd jnts
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
        selectBND = cmds.ls(sl=1)
        print selectBND

        # Bake anim to joints
        cmds.bakeResults(selectBND, t=(startTime, endTime))

        # Delete FK and IK joints+ctrls
        select(cl=1)
        cmds.select('*IK*', add=True)
        cmds.select('*FK*', add=True)
        cmds.select('*effector*', add=True)

        selectFKIK = cmds.ls(sl=1)
        cmds.delete(selectFKIK)

        # Select bnd jnts and xport as FBX
        select(cl=1)
        selectBNDJNTS()
        cmds.select('*_geo', add=True)

        toExport = cmds.ls(sl=True)

        cmds.select(toExport)
        # Not pretty but there is not exporting allowed in Python...
        preset_file = "{0}{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep,
                                         "UnityExport.fbxexportpreset").replace("\\", "/")
        mel.eval('FBXLoadExportPresetFile -f "{0}";'.format(preset_file))
        mel.eval('FBXExport -f "{0}" -s;'.format(scene_fbx.replace("\\", "/")))
        sys.stdout.write(">>>>> FBX with Animation Exported! <<<<<")
