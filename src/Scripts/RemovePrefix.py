# -*- coding: utf-8 -*-

# 特定の接頭辞を除きたい全てのモデルを選択した上で実行

from pyfbsdk import*

def RemovePrefix(mlist:FBModelList, prefix:str):
    for model in mlist:
        if model.Name.startswith(prefix):
            model.Name = model.Name.replace(prefix,"")

def main():
    mlist = FBModelList()
    FBGetSelectedModels(mlist)
    
    if len(mlist) == 0:
        FBMessageBox("Caution","You must select some models","OK")
    
    else:
        prefix = FBMessageBoxGetUserValue("Message", "prefix to omit", None,
                                       FBPopupInputType.kFBPopupString, "execute")
        RemovePrefix(mlist, prefix[1])        
        
if __name__ in ("__main__", "builtins"):
    main()