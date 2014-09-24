from pymel.all import *
from Truemax.checkNaming import get_top_node


def check_transforms():
    top_node = get_top_node()

    # Our top node is not correct and we can't check the transforms
    # until this is correct`
    if top_node is None:
        return True

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
            cmds.warning("%s has a none zero transform" % obj)
            problems = True
            select(cl=1)
            return False

    if problems is False:
        select(cl=1)
        return True