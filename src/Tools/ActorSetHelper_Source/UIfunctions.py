# -*- coding: utf-8 -*-

from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except: 
    from PySide2 import QtWidgets


from ui_ActorSetHelper import Ui_toolWidget
import BodyIndex


class ParentedWidget(QtWidgets.QWidget, Ui_toolWidget):
    def __init__(self, pWidgetHolder):
        super().__init__(pWidgetHolder)
        self.setupUi(self)


    # ActorとMarkerSetを作成
    def CreateActor_MarkerSet(self):
        self.actor = FBActor("HubActor")
        self.actor.MarkerSet = FBMarkerSet("MarkersetToHubActor")
        

    # 選択した一つのオブジェクトの位置にActorの腰を移動させる
    def FitToTrackers(self):
        targetmodel = FBModelList()
        targetposition = FBVector3d()
        FBGetSelectedModels(targetmodel)
        
        # モデルが選択されていない場合は選択するよう警告を表示
        if len(targetmodel) == 0:
            FBMessageBox("Caution", "Error : Select a target Model to fit", "OK")

        else:
            # 選択オブジェクトの位置を取得し、Actorの位置へ反映させる
            targetmodel[0].GetVector(targetposition, FBModelTransformationType.kModelTransformation)
            self.actor.SetActorTranslation(targetposition)


    # y軸中心にActorを180°回転させる
    def RotateYdeg(self):
        rlist = FBVector3d()

        # Actorの現時点の（腰の）回転座標を得る
        self.actor.GetDefinitionRotationVector(BodyIndex.AllActorIndex[0],rlist) 
        
        # 180°分の回転を加える
        self.actor.SetDefinitionRotationVector(BodyIndex.AllActorIndex[0],rlist + FBVector3d(0,180,0))
                

    # 直近に作成したActorとMarkerSetを削除し、Qt Sliderの位置を中心に戻す
    def ResetAll(self):
        msys = FBSystem()
        if len(msys.Scene.Actors) > 0 and len(msys.Scene.MarkerSets) > 0:  
            # 削除前に警告を表示
            check = FBMessageBox("Caution", "the Actor and MarkerSet will be removed.\n Are you sure you want to continue?", "Yes","No")
            
            if check == 1:
            # Scene内のActorとMarkerSetのうち、最後に作られたものを削除
                msys.Scene.Actors[-1].FBDelete()
                msys.Scene.MarkerSets[-1].FBDelete()

                # Qt Sliderの位置を初期の位置に戻す
                self.horizontalSlider.setSliderPosition(50)


    # Qt Sliderが動いた際にint値（Qt Designerで初期値50、1~100で変化するよう設定）を受け取り、Actorのサイズを変更
    def AdjustActorSize(self,int):
        for index in BodyIndex.AllActorIndex.values():
            self.actor.SetDefinitionScaleVector(index,FBVector3d(int/50,int/50,int/50)) 


    # MarkerSetにトラッカーを登録する
    def BindMarkerModel(self):    
        for tracker in BodyIndex.MarkerSetIndex.keys():
            model = FBFindModelByLabelName(tracker)
            for m in model.Children[0:4]:
                self.actor.MarkerSet.AddMarker(BodyIndex.MarkerSetIndex[tracker],m)

        # Snapを実行
        self.actor.Snap(FBRecalcMarkerSetOffset.kFBRecalcMarkerSetOffsetTR)

        FBMessageBox("message",
                    "Binding Tracker was completed !" + "\n" \
                    + "Let's play and animate Actor.","OK")