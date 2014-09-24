from pymel.all import *
import maya.cmds as cmds

SCENE_FILE_NAME_REGEX = r'[a-z]{2}[A-Z]{1}[a-zA-Z]+[A-Z]{1}_v[0-9]{3}_[a-z]{2}'
SCENE_FILE_TOP_NODE_REGEX = r'([a-z]{2}[A-Z]{1}[a-zA-Z]+[A-Z]{1})(_)'


def get_top_node(show_warnings=False):
    scene_file_raw = str(cmds.file(q=1, sceneName=1, shortName=1))

    def warning(str):
        if show_warnings:
            cmds.warning(str)
        return None

    if not re.match(SCENE_FILE_NAME_REGEX, scene_file_raw):
        return warning(">> Your scene file is named incorrectly <<")

    matches = re.search(SCENE_FILE_TOP_NODE_REGEX, scene_file_raw)
    if matches is None:
        return warning(">> Something went wrong... <<")

    groups = matches.groups()

    select(allDagObjects=1)
    all_top_nodes = cmds.ls(sl=1)
    if len(all_top_nodes) > 1:
        return warning(">> You have more than one top node! <<")

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

    children = cmds.listRelatives(top_node, children=True)

    named_correctly = True
    for c in children:
        if cmds.ls(c, showType=True)[1] == "mesh":
            continue

        if not (c.endswith("_geo") or c.endswith("_grp")):
            cmds.warning(">> %s is named incorrectly <<" % c)
            named_correctly = False

    return named_correctly