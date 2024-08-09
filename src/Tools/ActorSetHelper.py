
# -*- coding: utf-8 -*-

# 以下の指定配布先はデフォルトでモジュール探索パスに含まれる
# C:\Program Files\Autodesk\MotionBuilder <version>\bin\config\PythonStartup

from pyfbsdk import*
from pyfbsdk_additions import*
from ActorSetHelper_src import QWidgetConfigure

try:
    # MotionBuilder 2025 向け
    from PySide6.QtWidgets import QWidget
    from shiboken6 import wrapInstance, getCppPointer
     
except:
    # MotionBuilder 2024 向け
    from PySide2.QtWidgets import QWidget
    from shiboken2 import wrapInstance, getCppPointer    


# Qt製Widgetを保持するクラス
class WigHolder(FBWidgetHolder):
    
    # Qt製Widgetをインスタンス化するための、オーバーライドした関数
    def WidgetCreate(self, pParent):

        # wrapInstance()はポインターを不適切ではない任意の型に変換する
        parentwidget = wrapInstance(pParent, QWidget) 
        
        self.childwidget = QWidgetConfigure.ChildWidget(parentwidget)
        return getCppPointer(self.childwidget)[0]


# 大本のToolクラス
class tActorSetHelper(FBTool):
    def PopulateLayout(self):
        x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0, FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0, FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0, FBAttachType.kFBAttachBottom,"")
        
        # 子Widgetの表示領域を確保
        self.AddRegion("ChildWidget", "ActorSetHelper", x, y, w, h)
        
        # Qt製Widgetを保持したオブジェクトに対して、表示領域の制御を許可
        self.SetControl("ChildWidget", self.wigholder)

    def __init__(self, name):
        super().__init__(name)
        self.wigholder = WigHolder()
        self.PopulateLayout()

        # 初回表示サイズと最大・最小サイズの指定
        self.StartSizeX = 300
        self.StartSizeY = 275
        self.MinSizeX   = 200
        self.MinSizeY   = 175
        self.MaxSizeX   = 400
        self.MaxSizeY   = 375

def ActivateTool():
    # define the Tool name 
    toolName = "<tool name>"

    # check the Tool already created
    if toolName in FBToolList:
        ShowToolByName(toolName)

    else:
        # declare tool
        tool = tActorSetHelper(toolName)
        FBAddTool(tool)
        ShowToolByName(toolName)