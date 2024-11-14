# -*- coding: utf-8

from pathlib import Path
from pyfbsdk import FBGetMainWindow, FBApplication, ShowToolByName
from pyfbsdk_additions import FBToolList


# for MotionBuilder 2025
try:
    from PySide6.QtWidgets import QMainWindow, QMenuBar
    from shiboken6 import wrapInstance

# for MotionBuilder 2024
except:
    from PySide2.QtWidgets import QMainWindow, QMenuBar
    from shiboken2 import wrapInstance


# Get Menubar
def getMenubar() -> QMenuBar:
    pMainW = FBGetMainWindow()
    if pMainW:
        MainW = wrapInstance(pMainW, QMainWindow)
        menubar = MainW.menuWidget().children()[1]
        return menubar

# Add Menu in the Menubar
def AddMenu(mbar : QMenuBar):
    if mbar is not None:
        PluginBaseDir = Path(__file__).resolve().parent
        tools_dir   = PluginBaseDir / "Tools"
        scripts_dir = PluginBaseDir / "Scripts"

        # Add Empty Menu
        tmenu = mbar.addMenu("Tools")
        smenu = mbar.addMenu("Scripts")

        # if tools
        for tools_filepath in tools_dir.iterdir():
            if str(tools_filepath).endswith(".py"):
                FBApplication().ExecuteScript(str(tools_filepath))
                
                # add submenu
                module_name = tools_filepath.stem
                t = tmenu.addAction(module_name)
                t.triggered.connect(lambda check=False, name=module_name : ShowToolByName(name))
        
        # if scripts
        for script_filepath in scripts_dir.iterdir():
            if str(script_filepath).endswith(".py"):
                s = smenu.addAction(script_filepath.stem)
                s.triggered.connect(lambda check=False, sp = str(script_filepath) : FBApplication().ExecuteScript(sp))


if __name__ in ("__main__", "builtins"):
    menubar = getMenubar()
    AddMenu(menubar)