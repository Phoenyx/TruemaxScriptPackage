from Truemax.checkNaming import get_top_node
from Truemax.checkPivot import check_pivot
from Truemax.deleteDPLayers import deleteDPLayers
from Truemax.hfFixShading import hfFixBadShading
import maya.cmds as cmds
from pymel.all import mel


__author__ = 'sofiaelm'


# Runs all fixing scripts in the script package check list
def fixAllBelow():
    # Fix face assignment
    hfFixBadShading()
    # delete unused nodes
    mel.deleteUnusedNodes()
    # select top node
    cmds.select(get_top_node())
    # freeze transforms on top node
    mel.FreezeTransformations()
    # set pivot to origin
    mel.xform(zeroTransformPivots=1)
    # select hierarchy and freeze transforms
    cmds.select(hi=1)
    mel.FreezeTransformations()
    # delete history for all
    mel.DeleteHistory()
    # delete all display layers
    deleteDPLayers()

