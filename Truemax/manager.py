#!/usr/bin/python
# -*- coding: utf-8 -*-

import importlib
import os
import maya.cmds as cmds
from pymel.all import mel
import pymel.mayautils as mayautils
import ConfigParser
import shutil


class TruemaxModuleManager():
    title = "TruemaxPackage"
    version = "0.0.2"
    author = "Peter T, Sofia M, Daniel H"
    prefixName = "module"
    melScriptsDir = "melScripts"
    configFile = "config.ini"
    modules = []
    config = {}

    scripts = [{"name": "autoTangent", "version": "1.3m", "author": "Michael B. Comet"},
               {"name": "cometRename", "version": "1.2", "author": "Michael B. Comet"},
               {"name": "cometSaveSkinWeights", "version": "1.03", "author": "Michael B. Comet"},
               {"name": "DeleteUnusedNodes", "version": "1.0", "author": "Sofia M."},
               {"name": "dkAnim", "version": "0.98", "author": "Daniel Kramer"},
               {"name": "ExportFBX", "version": "1.0", "author": "Sofia M."},
               {"name": "jh_findDuplicateNames", "version": "1.0", "author": u"Jørn-Harald Paulsen"},
               {"name": "hfKillComponentShading", "version": "2.05", "author": "Henry Foster"},
               {"name": "hierarchySelection", "version": "1.0", "author": "Unknown"},
               {"name": "Image Plane-O-Rizer", "version": "1.0", "author": "Chris Whitaker"},
               {"name": "incrementalSave", "version": "1.0", "author": "Peter L. Thomasen"},
               {"name": "Joint-At-Pivot", "version": "1.0", "author": "Unknown"},
               {"name": "Mel-O-Matic", "version": "1.6", "author": "Andrew Osiow"},
               {"name": "NewScene", "version": "1.0", "author": "Sofia M."},
               {"name": "TurnTablePlayblast", "version": "1.0", "author": "Sofia M."},
               {"name": "PolyPlanarize", "version": "1.0", "author": "Chris Whitaker"},
               {"name": "PoseLib", "version": "6.2.3", "author": "Lionel Gallat"},
               {"name": "rbShapesWindow", "version": "1.0", "author": "Rasmus B"},
               {"name": "ReverseNormals", "version": "1.0", "author": "Sofia M."},
               {"name": "SetLocalPivot", "version": "1.0", "author": "Unknown"},
               {"name": "SetProject", "version": "1.0", "author": "Sofia M."},
               {"name": "thmbnailUpdTgl", "version": "1.0", "author": "Peter L. Thomasen"},
               {"name": "turnTablePlayblast", "version": "1.0", "author": "Sofia M."},
               {"name": "TweenMachine", "version": "2.04", "author": "Justin Barrett"},
               {"name": "wp_shapeParent", "version": "1.0", "author": "William Petruccelli"},
               {"name": "Vertex Paint SkinWeights", "version": "1.0", "author": "Unknown"},
               {"name": "ZeroJoint", "version": "1.0", "author": "Rasmus B"},
               {"name": "Zoomerator", "version": "1.0", "author": "Jeremie Talbot"}]

    def __init__(self, reloaded):
        self.read_config()
        self.load_modules()
        self.load_mel_scripts()
        self.create_ui()

        if reloaded:
            self.show_update_window()

    def load_modules(self):
        print "Loading Modules..."

        # Get all our python files that contains our prefix name
        # as the first characters and initialize them
        current_path = os.path.dirname(os.path.realpath(__file__))
        files = os.listdir(current_path)

        for f in files:
            name, ext = os.path.splitext(f)
            if name.startswith(self.prefixName) and ext == ".py":
                try:
                    name = "Truemax." + name
                    module = importlib.import_module(name, package=None)
                    module = reload(module)
                    print "Loaded {0}".format(name)

                    # Register the module
                    module_obj = module.initModule(self)
                    if isinstance(module_obj, Module):
                        self.modules.append(module_obj)
                    else:
                        print "{0} is not a module".format(name)

                except Exception as e:
                    print "Error loading module:"
                    print e

    def load_mel_scripts(self):
        print "Loading MEL files.."
        path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + self.melScriptsDir
        files = os.listdir(path)

        for f in files:
            name, ext = os.path.splitext(f)
            if ext == ".mel":
                file = path + os.path.sep + f
                file = file.replace("\\", "/")
                try:
                    mel.source(file)
                    print "Loaded {0}".format(f)
                except:
                    continue

    def create_ui(self):
        print "Creating UI..."

        # Create template
        template = "moduleManagerTemplate"
        window = "moduleManagerWindow"
        if cmds.uiTemplate(template, exists=1):
            cmds.deleteUI(template, uiTemplate=True)

        cmds.uiTemplate(template)
        cmds.frameLayout(defineTemplate=template, borderVisible=True, labelVisible=True, collapse=False, marginWidth=2,
                         marginHeight=2)
        cmds.columnLayout(adjustableColumn=True, defineTemplate=template, columnAttach=("both", 1))
        cmds.button(defineTemplate=template, label="Default Text")

        # Create window
        if cmds.window(window, exists=1):
            cmds.deleteUI(window, window=True)

        cmds.window(window, title=self.title, menuBar=True)
        cmds.setUITemplate(template, pushTemplate=1)

        # Create the menu
        cmds.menu(tearOff=False, label="Update")
        cmds.menuItem(command=lambda *args: self.update_scripts(), label="Network")

        cmds.menu(tearOff=False, label="Windows")
        cmds.menuItem(command=lambda *args: cmds.GraphEditor(), label="Graph Editor")
        cmds.menuItem(command=lambda *args: cmds.HypershadeWindow(), label="Hypershade")
        cmds.menuItem(command=lambda *args: cmds.OutlinerWindow(), label="Outliner")
        cmds.menuItem(command=lambda *args: cmds.ReferenceEditor(), label="Reference Editor")
        cmds.menuItem(command=lambda *args: cmds.ScriptEditor(), label="Script Editor")

        cmds.menu(helpMenu=True, tearOff=False, label="Help")
        cmds.menuItem(
            command=lambda *args: cmds.launch(web="http://download.autodesk.com/global/docs/maya2014/en_us/Commands/"),
            label="MEL Commands")
        cmds.menuItem(
            command=lambda *args: cmds.launch(
                web="http://download.autodesk.com/global/docs/maya2014/en_us/CommandsPython/"),
            label="PYTHON Commands")
        cmds.menuItem(
            command=lambda *args: cmds.launch(web="http://download.autodesk.com/global/docs/maya2014/en_us/Nodes/"),
            label="Nodes and Attributes")

        cmds.menuItem(divider=True)
        cmds.menuItem(command=self.openAboutWindow, label="About")

        # Create Version Frame
        cmds.frameLayout(label=(" Version " + str(self.version)))
        cmds.columnLayout(columnAttach=("both", 1))
        cmds.rowColumnLayout(numberOfColumns=2)
        cmds.textField('dateFld', width=175, editable=False, text=("Last Save: N/A"))
        cmds.button(width=110, command=lambda *args: mel.incrementalSave(), label="Incremental Save")
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        cmds.tabLayout('TabList')

        # Create tab UI for each module
        tabs = []
        for module in self.modules:
            tabs.append(module.create_ui())

        # Create Info Tab
        infoTab = self.create_info_tab()

        cmds.setParent('..')
        tabs.append((infoTab, "Info"))

        # Add Tabs / Show Window
        cmds.tabLayout('TabList', edit=1, tabLabel=tabs)
        cmds.showWindow(window)

        def dockWindow(window):
            dWindow = "moduleManagerDockedWindow"
            if cmds.dockControl(dWindow, exists=1):
                cmds.deleteUI(dWindow)

            formLayout = str(cmds.formLayout(parent=window))
            cmds.dockControl(dWindow, allowedArea="all", content=formLayout, area="right", label=self.title)
            cmds.control(window, p=formLayout, e=1, w=310)
            cmds.setParent('..')

        dockWindow(window)

    def create_info_tab(self):
        infoTab = str(cmds.columnLayout())
        cmds.separator(style="none")
        cmds.separator(style="in")
        cmds.text(label="")

        def createRow(title, version, author):
            cmds.rowLayout(
                columnAttach=[(1, "both", 0), (2, "both", 0), (3, "both", 0), (4, "both", 0), (5, "both", 0)],
                numberOfColumns=5,
                adjustableColumn=5,
                columnAlign=[(1, "right"), (2, "center"), (3, "left"), (4, "center"), (5, "left")],
                columnWidth5=(120, 10, 25, 10, 150))
            cmds.text(label=title)
            cmds.text(label="")
            cmds.text(label=version)
            cmds.text(label="")
            cmds.text(label=author)
            cmds.setParent('..')


        # Create rows for modules
        for m in self.modules:
            for s in m.scripts:
                createRow(s["name"], s["version"], s["author"])

        # Create rows for manager scripts
        for s in self.scripts:
            createRow(s["name"], s["version"], s["author"])

        # Create row for this script
        createRow(self.title, self.version, self.author)
        return infoTab

    def openAboutWindow(self, *args):
        if cmds.window("scriptPackageAboutWindow", exists=1):
            cmds.deleteUI("scriptPackageAboutWindow")

        def closeAboutWindow(*args):
            cmds.deleteUI("scriptPackageAboutWindow")

        scriptPackageAboutWindow = str(cmds.window("scriptPackageAboutWindow", sizeable=False, title="About"))

        cmds.columnLayout(width=306, adjustableColumn=True)
        cmds.text(width=306, label="")
        cmds.text(
            label="Feel free to copy, share or modify 'ScriptPackage' as you please, except for commercial purposes.")
        cmds.text(
            label="All scripts/plugins that runs from 'ScriptPackage' are copyrighted by their respective owners.")
        cmds.button(width=150, command=closeAboutWindow, label="Close")
        cmds.showWindow(scriptPackageAboutWindow)

    def read_config(self):
        Config = ConfigParser.ConfigParser()

        def map_config(section):
            dict1 = {}
            options = Config.options(section)
            for option in options:
                try:
                    dict1[option] = Config.get(section, option)
                except:
                    dict1[option] = None
            return dict1

        try:
            file = "{0}{1}..{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep, self.configFile)
            Config.read(file)
            section = "TruemaxManager"
            self.config = map_config(section)
        except Exception as e:
            print "Failed reading config"
            print e

    def update_scripts(self):
        if "downloadlocation" in self.config:
            location = self.config["downloadlocation"]
            current_location = "{0}{1}..{1}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep)

            if os.path.exists(location):
                files = os.listdir(location)
                for f in files:
                    try:
                        if f != "Truemax" and f != "userSetup.py":
                            continue

                        full_path = location + os.path.sep + f
                        dest_path = current_location + os.path.sep + f
                        if os.path.isfile(full_path):
                            shutil.copyfile(full_path, dest_path)
                        else:
                            if os.path.exists(dest_path):
                                shutil.rmtree(dest_path)
                            shutil.copytree(full_path, dest_path)
                    except Exception as e:
                        print "Unable to copy {0}".format(f)
                        print e
                        continue

                self.reload_self()
            else:
                print "Location {0} doesn't exist".format(location)
        else:
            print "Unable to download scripts as location is unknown."

    def reload_self(self):
        file = "{0}{1}..{1}{2}".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep, "userSetup.py")
        mayautils.source(file)

    def show_update_window(self):
        window = "truemaxUpdateWindow"

        # Create window
        if cmds.window(window, exists=1):
            cmds.deleteUI(window, window=True)

        def closeWindow(*args):
            cmds.deleteUI(window)

        cmds.window(window, sizeable=False, title="Update")

        self.create_info_tab()
        cmds.button(width=350, command=closeWindow, label="Close")

        cmds.showWindow(window)


class Module():
    scripts = []

    def __init__(self, moduleManager):
        return

    def run(self):
        print "You need to create your function."

    def create_ui(self):
        return
