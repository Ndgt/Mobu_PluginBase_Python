# -*- coding: utf-8

import sys,os,inspect,importlib
from pyfbsdk import FBGetMainWindow

# for MotionBuilder 2025
try:
    from PySide6 import QtWidgets
    from shiboken6 import wrapInstance

# for MotionBuilder -2024
except:
    from PySide2 import QtWidgets
    from shiboken2 import wrapInstance


# get the widget of Motionbuilder main window 
def getMainWindow() -> QtWidgets.QWidget:
    ptr = FBGetMainWindow()
    if ptr is not None:
        # convert the pointer to QWidget instance
        return wrapInstance(ptr, QtWidgets.QWidget)


# search and return TabMenu Widget 
def getTabMenu(win : QtWidgets.QWidget) -> QtWidgets.QMenu:
    if win is not None:
        # Search TabMenu Widget
        for child in win.children():
            if not str(type(child)).find("QtWidgets.QWidget") == -1:
                for childwidget in child.children():
                    if not str(type(childwidget)).find("QtWidgets.QMenuBar") == -1:
                        return childwidget

# Add menu in TabMenu
def AddMenu(tabmenu : QtWidgets.QMenu):
    if tabmenu is not None:
        toolList = []
        scriptList = []

        # add module search path to Tools / Scripts directory
        CurrentFilePath = inspect.currentframe().f_code.co_filename
        CurrentDir = os.path.dirname(CurrentFilePath)
        toolpath = os.path.join(CurrentDir,"Tools")
        scriptpath = os.path.join(CurrentDir,"Scripts")
        sys.path.append(toolpath)
        sys.path.append(scriptpath)

        # add TabMenu
        tmenu = tabmenu.addMenu("Tools")
        smenu = tabmenu.addMenu("Scripts")


        for file in os.listdir(toolpath):
            if file.endswith(".py"):
                module_name = file[:-3]
                module = importlib.import_module(module_name)
                
                # add submenu and connect module
                t = tmenu.addAction(module_name)
                t.triggered.connect(module.ActivateTool)
        
        for file in os.listdir(scriptpath):
            if file.endswith(".py"):
                module_name = file[:-3]
                module = importlib.import_module(module_name)

                # add submenu and connect module
                s = smenu.addAction(module_name)
                s.triggered.connect(module.main)


if __name__ in ("__main__", "builtins"):
    mainwindow = getMainWindow()
    tabmenu = getTabMenu(mainwindow)
    AddMenu(tabmenu)