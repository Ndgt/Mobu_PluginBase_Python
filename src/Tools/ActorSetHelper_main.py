# -*- coding: utf-8 -*-

from pyfbsdk import*
from pyfbsdk_additions import*

try:
    # for MotionBuilder 2025
    from PySide6 import QtWidgets
    from shiboken6 import wrapInstance, getCppPointer
     
except:
    # for MotionBuilder -2024
    from PySide2 import QtWidgets
    from shiboken2 import wrapInstance, getCppPointer    


# このファイルのパスを取得し、一つ下の階層のActorSetHelper_Sourceにモジュール検索パスを通す
import sys,os,inspect
CurrentFilePath = inspect.currentframe().f_code.co_filename
CurrentDir = os.path.dirname(CurrentFilePath)
targetPath = os.path.join(CurrentDir,"ActorSetHelper_Source")
sys.path.append(targetPath)

import UIfunctions


class WidgetHolder(FBWidgetHolder):
    def WidgetCreate(self, pWigParent):
        self.ParentedWidgetObject = UIfunctions.ParentedWidget(wrapInstance(pWigParent, QtWidgets.QWidget))
        return getCppPointer(self.ParentedWidgetObject)[0]


class WigTool(FBTool):
    def PopulateLayout(self):
        x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0, FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0, FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0, FBAttachType.kFBAttachBottom,"")
        self.AddRegion("ParentedWidget", "ActorSetHelper", x,y,w,h)
        self.SetControl("ParentedWidget", self.WidgetHolderObject)

    def __init__(self,name):
        super().__init__(name)
        self.WidgetHolderObject = WidgetHolder()
        self.PopulateLayout()
        self.StartSizeX = 300
        self.StartSizeY = 275


def ActivateTool():
    # Toolの名前を設定
    toolName = "ActorSetHelper"

    if toolName in FBToolList:
        ShowToolByName(toolName)
    
    else:
        # Toolを作成し、Python Tool Managerに加える
        tool = WigTool(toolName)
        FBAddTool(tool)
        ShowToolByName(toolName)