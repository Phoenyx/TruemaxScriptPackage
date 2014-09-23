from pymel.all import *


def check_transforms():
    scene_file_raw = str(cmds.file(q=1, sceneName=1, shortName=1))
    topNode = str(mel.match("[a*-z]+[A-Z]", scene_file_raw))

    select(topNode)
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