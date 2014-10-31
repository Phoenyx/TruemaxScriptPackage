from Truemax.checkNaming import get_top_node
from hfFixShading import hfCheckShading

__author__ = 'sofiaelm'

from pymel.all import *


def detect_history():

    top_node = get_top_node()

    #Delets groupIds created by hfFixShading script:
    if hfCheckShading() is False:
        unused_stuff = cmds.ls('*hyperLayout*', '*hyperView*', '*nodeEditorPanel*', '*nodeView*', '*groupId*')

        if unused_stuff != []:
            cmds.delete(unused_stuff)


    # Our top node is not correct and we can't check the history
    # until this is correct`
    if top_node is None:
        return True

    select(top_node)
    select(hi=1)
    select("*Shape*", deselect=1)
    select(top_node, deselect=1)
    objects = cmds.ls(sl=1)

    for obj in objects:
        history = cmds.listHistory(obj)
        if len(history) > 1:
            cmds.warning(">> %s has construction history or face assignment! <<" % obj)
            return False

    return True