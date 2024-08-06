# -*- coding: utf-8

import os, sys, inspect, importlib
from pyfbsdk import FBGetMainWindow

# for MotionBuilder 2025
try:
    from PySide6.QtWidgets import QMainWindow, QMenuBar
    from shiboken6 import wrapInstance

# for MotionBuilder -2024
except:
    from PySide2.QtWidgets import QMainWindow, QMenuBar
    from shiboken2 import wrapInstance


# get menubar
def getMenubar() -> QMenuBar:
    pMainW = FBGetMainWindow()
    if pMainW:
        MainW = wrapInstance(pMainW, QMainWindow)
        menubar = MainW.menuWidget().children()[1]
        return menubar

# Add menu in MenuBar
def AddMenu(mbar : QMenuBar):
    if mbar is not None:
        CurrentFilePath = inspect.currentframe().f_code.co_filename
        CurrentDir = os.path.dirname(CurrentFilePath)

        # directories to store original Tools/Scripts
        toolpath   = os.path.join(CurrentDir,"Tools")
        scriptpath = os.path.join(CurrentDir,"Scripts")

        # add module search path to Tools/Scripts directory        
        sys.path.append(toolpath)
        sys.path.append(scriptpath)

        # add menu in TabMenu
        tmenu = mbar.addMenu("Tools")
        smenu = mbar.addMenu("Scripts")

        # if Tools
        for file in os.listdir(toolpath):
            if file.endswith(".py"):
                module_name = file[:-3]
                module = importlib.import_module(module_name)
                
                # add submenu and connect module
                t = tmenu.addAction(module_name)
                t.triggered.connect(module.ActivateTool)
        
        # if Scripts
        for file in os.listdir(scriptpath):
            if file.endswith(".py"):
                module_name = file[:-3]
                module = importlib.import_module(module_name)

                # add submenu and connect module
                s = smenu.addAction(module_name)
                s.triggered.connect(module.main)


if __name__ in ("__main__", "builtins"):
    menubar = getMenubar()
    AddMenu(menubar)