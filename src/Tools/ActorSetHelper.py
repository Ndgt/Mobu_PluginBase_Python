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
        
        # region name, display name, x,y,w,h
        self.AddRegion("ParentedWidget", "ActorSetHelper", x,y,w,h)
        
        # give a Control in the region to the Widget object
        self.SetControl("ParentedWidget", self.WidgetHolderObject)

    def __init__(self,name):
        super().__init__(name)
        self.WidgetHolderObject = WidgetHolder()
        self.PopulateLayout()

        # set the size of UI first displayed
        self.StartSizeX = 300
        self.StartSizeY = 275


'''
This Function Must Be Defined
'''
def ActivateTool():
    # define the Tool name
    toolName = "ActorSetHelper"

    # check the Tool already created
    if toolName in FBToolList:
        ShowToolByName(toolName)
    
    else:
        # declare tool
        tool = WigTool(toolName)
        FBAddTool(tool)
        ShowToolByName(toolName)