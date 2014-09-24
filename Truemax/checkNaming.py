from pymel.all import *
import maya.cmds as cmds

SCENE_FILE_NAME_REGEX = r'[a-z]{2}[A-Z]{1}[a-zA-Z]+[A-Z]{1}_v[0-9]{3}_[a-z]{2}'
SCENE_FILE_TOP_NODE_REGEX = r'([a-z]{2}[A-Z]{1}[a-zA-Z]+[A-Z]{1})(_)'


def name_compare():
    # Is their scene name correct?
    scene_file_raw = str(cmds.file(q=1, sceneName=1, shortName=1))

    if not re.match(SCENE_FILE_NAME_REGEX, scene_file_raw):
        print ">> Your scene file is named incorrectly <<"
        return False

    matches = re.search(SCENE_FILE_TOP_NODE_REGEX, scene_file_raw)
    if matches is None:
        print ">> Something went wrong... <<"
        return False

    groups = matches.groups()

    select(allDagObjects=1)
    all_top_nodes = cmds.ls(sl=1)
    if (len(all_top_nodes) > 1):
        print ">> You have more than one top node! <<"
        return False

    if len(groups) != 2:
        print ">> Something went wrong... <<"
        return False

    if groups[0] not in cmds.ls():
        print ">> Your top node is not named correctly <<"
        return False

    top_node = groups[0]

    if cmds.listRelatives(top_node, allParents=True) is not None:
        print ">> Top node has a parent <<"
        return False

    children = cmds.listRelatives(top_node, children=True)

    named_correctly = True
    for c in children:
        if cmds.ls(c, showType=True)[1] == "mesh":
            continue

        if not (c.endswith("_geo") or c.endswith("_grp")):
            print ">> %s is named incorrectly <<" % c
            named_correctly = False

    return named_correctly