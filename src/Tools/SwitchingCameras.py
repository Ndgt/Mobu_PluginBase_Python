# -*- coding: utf-8 -*-

from pyfbsdk import *
from pyfbsdk_additions import *

def SwitchCamera(pControl, pEvent):
    renderer = FBSystem().Scene.Renderer
    camIndex = pControl.ItemIndex
    ActivePaneIndex = renderer.GetSelectedPaneIndex()
    if renderer.GetSchematicViewPaneIndex() == ActivePaneIndex:
        renderer.SetSchematicViewInPane(ActivePaneIndex, False)
    if pControl.ItemIndex == 7:
        renderer.SetSchematicViewInPane(ActivePaneIndex, True)
        return
    elif pControl.ItemIndex < 7:
        renderer.SetCameraInPane(FBSystem().Scene.Cameras[camIndex], ActivePaneIndex)

def PopulateLayout(tool:FBTool):
    x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
    y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,"")
    w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
    h = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"")
    tool.AddRegion("MainRegion","RegionName", x, y, w, h)
    
    vbox = FBVBoxLayout( FBAttachType.kFBAttachTop )
    tool.SetControl("MainRegion",vbox)
    
    List1 = FBList()
    List1.style = FBListStyle.kFBDropDownList

    camList = FBSystem().Scene.Cameras
    for i in range(len(camList)):
        # list item must be string
        List1.Items.append(camList[i].Name)
    List1.Items.append("Schematic View")    
    List1.OnChange.Add(SwitchCamera)
    
    vbox.Add(List1, 30, space = 10)
    
    
# do not show the tool, just create
t = FBCreateUniqueTool("SwitchingCameras")
t.StartSizeX = 200
t.StartSizeY = 100
PopulateLayout(t) 
FBAddTool(t)