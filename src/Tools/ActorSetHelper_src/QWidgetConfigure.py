# -*- coding: utf-8 -*-

from pyfbsdk import*
from ActorSetHelper_src.QWidgetDetails import Ui_childWidget
from ActorSetHelper_src import BodyIndex

try:
    from PySide6.QtWidgets import QWidget
except: 
    from PySide2.QtWidgets import QWidget


class ChildWidget(QWidget, Ui_childWidget):
    def __init__(self, pParent):
        super().__init__(pParent)
        self.setupUi(self)
        self.actor = None

    # メンバself.actorの格納状態をチェック
    def check_actor_exists(self):
        if self.actor is None:
            return False
        return True

    # ActorとMarkerSetを作成
    def CreateActor_MarkerSet(self):
        if self.actor is not None:
            FBMessageBox("Caution", "Error : You already created actor.\n Press \"Reset\" button.", "OK")
            return

        self.actor = FBActor("NewActor")
        self.actor.MarkerSet = FBMarkerSet("NewMarkerSet")
        

    # 選択した一つのオブジェクトの位置にActorの腰を移動させる
    def FitToTrackers(self):
        targetmodels = FBModelList()
        targetposition = FBVector3d()
        FBGetSelectedModels(targetmodels)
        
        # モデルが選択されていない場合は選択するよう警告を表示
        if len(targetmodels) == 0:
            FBMessageBox("Caution", "Error : Select a target Model to fit", "OK")
            return

        else:
            # 選択オブジェクトの位置を取得し、Actorの位置へ反映させる
            targetmodels[0].GetVector(targetposition, FBModelTransformationType.kModelTransformation)
            self.actor.SetActorTranslation(targetposition)

            # 全ての選択オブジェクトの選択状態を解除する
            for model in targetmodels:
                model.Selected = False


    # y軸中心にActorを180°回転させる
    def RotateYdeg(self):
        rlist = FBVector3d()

        if not self.check_actor_exists():
            return

        # Actorの現時点の（腰の）回転座標を得る
        self.actor.GetDefinitionRotationVector(BodyIndex.AllActorIndex[0],rlist) 
        
        # 180°分の回転を加える
        self.actor.SetDefinitionRotationVector(BodyIndex.AllActorIndex[0],rlist + FBVector3d(0,180,0))
                

    # リセット。直近に作成したActorとMarkerSetを削除し、Qt Sliderの位置を中心に戻す
    def ResetAll(self):
        msys = FBSystem()
        if len(msys.Scene.Actors) > 0 and len(msys.Scene.MarkerSets) > 0:  
            # 削除前に警告を表示
            check = FBMessageBox("Caution", "the Actor and MarkerSet will be removed.\n Are you sure you want to continue?", "Yes","No")
            
            if check == 1:
            # Scene内のActorとMarkerSetのうち、最後に作られたものを削除
                if len(msys.Scene.Actors) > 0:
                    msys.Scene.Actors[-1].FBDelete()
                if len(msys.Scene.MarkerSets) > 0:
                    msys.Scene.MarkerSets[-1].FBDelete()

                # クラスメンバをNoneで上書き
                self.actor = None

                # Qt Sliderの位置を初期の位置に戻す
                self.horizontalSlider.setSliderPosition(50)

        else:
            self.actor = None
            self.horizontalSlider.setSliderPosition(50)


    # Qt Sliderが動いた際にint値（Qt Designerで初期値50、1~100で変化するよう設定）を受け取り、Actorのサイズを変更
    def AdjustActorSize(self,int):
        if not self.check_actor_exists():
            return
        
        for index in BodyIndex.AllActorIndex.values():
            self.actor.SetDefinitionSzcaleVector(index,FBVector3d(int/50,int/50,int/50)) 


    # MarkerSetにトラッカーを登録する
    def BindMarkerModel(self):
        if not self.check_actor_exists():
            return

        # 既にsnapを実行してActiveになっていたら登録作業はしない
        if self.actor.Active == True:
            FBMessageBox("Caution", "Error : The Actor Set is already Active", "OK")
            return
        
        for tracker in BodyIndex.MarkerSetIndex.keys():
            model = FBFindModelByLabelName(tracker)
            for m in model.Children[0:4]:
                self.actor.MarkerSet.AddMarker(BodyIndex.MarkerSetIndex[tracker],m)

        # Snapを実行
        SnapSuccess = self.actor.Snap(FBRecalcMarkerSetOffset.kFBRecalcMarkerSetOffsetTR)
        if not SnapSuccess:
            FBMessageBox("Caution", "Error : Snap was not succeeded.", "OK")
            return
            #
            # ここの例外処理分からん
            # snapが成功しない場合の例としては、トラッカーの登録が不十分（頭が登録できてないなど）の場合
            #

        FBMessageBox("message",
                    "Binding Tracker was completed !" + "\n" +
                    "Let's play and animate Actor.","OK")