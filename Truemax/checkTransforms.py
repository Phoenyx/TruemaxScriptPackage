from pymel.all import *


def check_transforms():
    SCENE_FILE_NAME_REGEX = r'[a-z]{2}[A-Z]{1}[a-zA-Z]+[A-Z]{1}_v[0-9]{3}_[a-z]{2}'
    SCENE_FILE_TOP_NODE_REGEX = r'([a-z]{2}[A-Z]{1}[a-zA-Z]+[A-Z]{1})(_)'

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

    if len(groups) != 2:
        print ">> Something went wrong... <<"
        return False

    if groups[0] not in cmds.ls():
        print ">> Your top node is not named correctly <<"
        return False

    top_node = groups[0]
    select(top_node)
    select(hi=1)
    select(("*Shape*"), deselect=1)
    objects = ls(sl=1)

    problems = False
    for obj in objects:
        if not (getAttr(obj + '.translateX') == 0 and getAttr(obj + '.translateY') == 0 and getAttr(
                    obj + '.translateZ') == 0 and getAttr(obj + '.rotateX') == 0 and getAttr(
                    obj + '.rotateY') == 0 and getAttr(obj + '.rotateZ') == 0 and getAttr(
                    obj + '.scaleX') == 1 and getAttr(obj + '.scaleX') == 1 and getAttr(obj + '.scaleX') == 1):
            problems = True
            select(cl=1)
            return False

    if problems is False:
        select(cl=1)
        return True