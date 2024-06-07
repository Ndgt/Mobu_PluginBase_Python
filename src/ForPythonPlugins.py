# -*- coding: utf-8

import sys,os,inspect,importlib
from pyfbsdk import FBGetMainWindow, ShowToolByName
from pyfbsdk_additions import FBToolList

# for MotionBuilder 2025
try:
    from PySide6 import QtWidgets
    from shiboken6 import wrapInstance

# for MotionBuilder -2024
except:
    from PySide2 import QtWidgets
    from shiboken2 import wrapInstance


# メニュー押下時にツールを表示
def FromMenuActivate(Name:str):
    if Name in FBToolList:
        ShowToolByName(Name)

    else:
        script = importlib.import_module(Name)
        script.main()

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


def ReturnList() -> tuple[list,list]:
    toolList = []
    scriptList = []

    CurrentFilePath = inspect.currentframe().f_code.co_filename
    CurrentDir = os.path.dirname(CurrentFilePath)
    toolpath = os.path.join(CurrentDir,"Tools")
    scriptpath = os.path.join(CurrentDir,"Scripts")
    sys.path.append(toolpath)
    sys.path.append(scriptpath)

    for file in os.listdir(toolpath):
        if file.endswith(".py"):
            module_name = file - ".py"
            importlib.import_module(module_name)
            toolList.append(module_name)
    
    for file in os.listdir(scriptpath):
        if file.endswith(".py"):
            module_name = file - ".py"
            importlib.import_module(module_name)
            scriptList.append(module_name)

    return toolList,scriptList


if __name__ in ("__main__", "__builtins__"):
    mainwindow = getMainWindow()
    tabwidget = getTabMenu(mainwindow)
    
    tmenu = tabwidget.addMenu("Tools")
    smenu = tabwidget.addMenu("Scripts")

    for toolName, scriptName in ReturnList():
        t = tmenu.addAction(toolName)
        t.triggered.connect(FromMenuActivate, toolName)
        s = smenu.addAction(scriptName)
        s.triggered.connect(FromMenuActivate, scriptName)