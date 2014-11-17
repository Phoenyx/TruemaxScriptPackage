from pymel.all import *
import maya.cmds as cmds

SCENE_FILE_NAME_REGEX = r'[a-z]{2}[A-Z]{1}[a-zA-Z]+[A-Z]{1}_v[0-9]{3}_[a-zA-Z]{2}'
SCENE_FILE_TOP_NODE_REGEX = r'([a-z]{2}[A-Z]{1}[a-zA-Z]+[A-Z]{1})(_)'


def get_top_node(show_warnings=False):
    def warning(str):
        if show_warnings:
            cmds.warning(str)
        return None

    scene_file_raw = str(cmds.file(q=1, sceneName=1, shortName=1))

    if not re.match(SCENE_FILE_NAME_REGEX, scene_file_raw):
        return warning(">> Your scene file is named incorrectly <<")

    matches = re.search(SCENE_FILE_TOP_NODE_REGEX, scene_file_raw)
    if matches is None:
        return warning(">> Something went wrong... <<")

    groups = matches.groups()

    if len(groups) != 2:
        return warning(">> Something went wrong... <<")

    if groups[0] not in cmds.ls():
        return warning(">> Your top node is not named correctly <<")

    top_node = groups[0]

    if cmds.listRelatives(top_node, allParents=True) is not None:
        return warning(">> Top node has a parent <<")

    return top_node


def name_compare():
    # Is their scene name correct?
    top_node = get_top_node(show_warnings=True)

    # Exit as our top_node is not found
    if top_node is None:
        return False

    children = cmds.listRelatives(top_node, allDescendents=True)

    named_correctly = True
    for c in children:
        if not cmds.ls(c, showType=True)[1] == "transform":
            continue

        if not (c.endswith("_geo") or c.endswith("_grp") or c.endswith("_ctrl")):
            cmds.warning(">> %s is named incorrectly <<" % c)
            named_correctly = False


    # List all materials in scene
    all_materials = cmds.ls(materials=True)

    # See if any are named incorrectly. Allow initialshadinggroup (lambert1) and particle shader (particleCloud1).
    # if a shader ends with "SHD" we assume its named correctly.

    for mat in all_materials:
        if not (mat.endswith(top_node+"SHD") or mat.endswith("lambert1") or mat.endswith("particleCloud1")):
            cmds.warning(">> %s is named incorrectly <<" % mat)
            named_correctly = False

    return named_correctly


