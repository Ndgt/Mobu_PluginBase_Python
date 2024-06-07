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
# MotionBuilderのUI全体の親にあたるwidgetを取得
def getMainWindow() -> QtWidgets.QWidget:
    ptr = FBGetMainWindow()
    if ptr is not None:
        return wrapInstance(ptr, QtWidgets.QWidget)


def getTabMenu(win : QtWidgets.QWidget) -> QtWidgets.QMenu:
    if win is not None:
        # 画面上部のメニュータブのwidgetが見つかるまで子を探索
        # どちらのPySideのバージョンにも対応すべく、型そのものではなく型の文字列で条件分岐
        for child in win.children():
            if not str(type(child)).find("QtWidgets.QWidget") == -1:
                for childwidget in child.children():
                    if not str(type(childwidget)).find("QtWidgets.QMenuBar") == -1:
                        return childwidget


def AddMenu(tabmenu:QtWidgets.QMenu) -> tuple[list,list]:
    toolList = []
    scriptList = []

    CurrentFilePath = inspect.currentframe().f_code.co_filename
    CurrentDir = os.path.dirname(CurrentFilePath)
    toolpath = os.path.join(CurrentDir,"Tools")
    scriptpath = os.path.join(CurrentDir,"Scripts")
    sys.path.append(toolpath)
    sys.path.append(scriptpath)

    tmenu = tabmenu.addMenu("Tools")
    smenu = tabmenu.addMenu("Scripts")

    for file in os.listdir(toolpath):
        if file.endswith(".py"):
            module_name = file[:-3]
            module = importlib.import_module(module_name)
            t = tmenu.addAction(module_name)
            t.triggered.connect(module.ActivateTool)
    
    for file in os.listdir(scriptpath):
        if file.endswith(".py"):
            module_name = file[:-3]
            module = importlib.import_module(module_name)
            s = smenu.addAction(module_name)
            s.triggered.connect(module.main)


if __name__ in ("__main__", "builtins"):
    mainwindow = getMainWindow()
    tabmenu = getTabMenu(mainwindow)
    AddMenu(tabmenu)