__author__ = 'sofiaelm'

def set_settings():
    self.setProjectAsCurrDirectory()
    cmds.currentUnit(linear='m')

    if cmds.pluginInfo('fbxmaya', query=True, loaded=True) == False:
        cmds.loadPlugin('fbxmaya', quiet=True)
        cmds.pluginInfo('fbxmaya', edit=True, autoload=True)

    # Set the far clipping plane to 10,000
    cmds.camera(farClipPlane=10000)
    cmds.select(cl=1)