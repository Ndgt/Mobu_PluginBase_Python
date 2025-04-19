from pyfbsdk import FBModel, FBNamespaceAction, FBSystem, FBMatrix

def DeepModelClone(model_root: FBModel) -> None:
    """最上位のノードから階層を保持してオブジェクトをコピー"""

    def GetNamespaceStr(model: FBModel) -> str:
        """モデルの namespace名を返す"""
        colon_index = model.LongName.find(":")
        if colon_index != -1:
            return model.LongName[0:colon_index]
        else:
            return ""

    def UpdateNamespace(model: FBModel, model_clone: FBModel) -> None:
        """コピーしたモデルのnamespaceを、元のモデルのnamespaceに沿ったものに更新"""
        namespace_original = GetNamespaceStr(model)
        if namespace_original:
            namespace_created = GetNamespaceStr(model_clone)
            namespace_copy = namespace_original + "_copied"
            model_clone.ProcessObjectNamespace(
                FBNamespaceAction.kFBReplaceNamespace,
                namespace_created,
                namespace_copy,
                False
            )

    def RetriveModelTranform(model: FBModel, model_clone: FBModel) -> None:
        """モデルの Transform をコピー"""
        transform_original = FBMatrix()
        model.GetMatrix(transform_original)
        model_clone.SetMatrix(transform_original)
        
    def CloneChildModels(model_parent: FBModel, model_parent_clone: FBModel) -> None:
        """モデルのコピーを再帰的に実行"""
        if len(model_parent.Children) > 0:
            for model_child in model_parent.Children:
                # Clone およびペアレント化
                model_child_clone = model_child.Clone()
                model_child_clone.Parent = model_parent_clone

                # Transform のコピー
                RetriveModelTranform(model_child, model_child_clone)
                
                # namespace 更新
                namespace_created = GetNamespaceStr(model_child_clone)
                if namespace_created:
                    UpdateNamespace(model_child, model_child_clone)

                    # 使用されなくなった namespace を削除
                    FBSystem().Scene.NamespaceDelete(namespace_created)

                CloneChildModels(model_child, model_child_clone)

    if isinstance(model_root, FBModel):
        model_root_clone = model_root.Clone()
        if GetNamespaceStr(model_root):
            UpdateNamespace(model_root, model_root_clone)
        CloneChildModels(model_root, model_root_clone)