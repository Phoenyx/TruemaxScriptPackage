# Start our module manager rolling
import maya.cmds as cmds

def loadUser(reloaded=False):
    import Truemax.manager as moduleman
    print "Running User Setup"
    reload(moduleman)
    mm = moduleman.TruemaxModuleManager(reloaded)

if __name__ == "__main__":
    # Defer this until maya is ready for us
    cmds.evalDeferred("loadUser()")

if __name__ == "pymel.mayautils":
    loadUser(True)