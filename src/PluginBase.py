# -*- coding: utf-8

import importlib
from pathlib import Path
from pyfbsdk import FBGetMainWindow, FBApplication


# MotionBuilder 2025 向け
try:
    from PySide6.QtWidgets import QMainWindow, QMenuBar
    from shiboken6 import wrapInstance

# for MotionBuilder 2024 向け
except:
    from PySide2.QtWidgets import QMainWindow, QMenuBar
    from shiboken2 import wrapInstance


# メニューバーの取得
def getMenubar() -> QMenuBar:
    pMainW = FBGetMainWindow()
    if pMainW:
        MainW = wrapInstance(pMainW, QMainWindow)
        menubar = MainW.menuWidget().children()[1]
        return menubar

# メニューバーへのメニューの追加
def AddMenu(mbar : QMenuBar):
    if mbar is not None:
        PluginBaseDir = Path(__file__).resolve().parent

        # 独自のツールおよびスクリプトを格納する先のディレクトリ
        tools_dir   = PluginBaseDir / "Tools"
        scripts_dir = PluginBaseDir / "Scripts"

        # 空のメニューを追加
        tmenu = mbar.addMenu("Tools")
        smenu = mbar.addMenu("Scripts")

        # ツールの場合
        for tools_filepath in tools_dir.iterdir():
            if str(tools_filepath).endswith(".py"):
                module_name = tools_filepath.stem
                module = importlib.import_module(module_name)
                
                # add submenu and connect module
                t = tmenu.addAction(module_name)
                t.triggered.connect(module.ActivateTool)
        
        # スクリプトの場合
        for script_filepath in scripts_dir.iterdir():
            if str(script_filepath).endswith(".py"):
                s = smenu.addAction(script_filepath.stem)
                s.triggered.connect(lambda check=False, sp = str(script_filepath) : FBApplication().ExecuteScript(sp))

if __name__ in ("__main__", "builtins"):
    menubar = getMenubar()
    AddMenu(menubar)