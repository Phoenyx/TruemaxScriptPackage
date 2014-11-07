

__author__ = 'sofiaelm'
# version 1.0
# Tool that detects if the object has construction history

from pymel.all import *
from Truemax.checkNaming import get_top_node
from hfFixShading import hfCheckShading

def detect_history():

    top_node = get_top_node()
    if top_node is None:
        return True
    # if the top node is not named correctly or non existent we cannot check the history.

    # select the hierarchy
    select(top_node)
    select(hi=1)

    # Deselect the shapes
    select("*Shape*", deselect=1)

    # Some props have been rigged with constraints, we don't want to check the history on them.
    if cmds.objExists("*orientConstraint*") == 1:
        select("*orientConstraint*", deselect=1)

    # Make a list of the selection
    select(top_node, deselect=1)
    objects = cmds.ls(sl=1)

    # Check all elements in the selection for construction history.
    for obj in objects:
        history = cmds.listHistory(obj)
        if len(history) > 1:
            cmds.warning(">> %s has construction history! <<" % obj)
            return False

    return True

    # We return a bool for the CheckList script to pick up.
