# -*- coding: utf-8 -*-

# Note : select models before execute

from pyfbsdk import (FBModelList, FBGetSelectedModels, FBMessageBox,
                     FBMessageBoxGetUserValue, FBPopupInputType)

# initialize input
prefix = ""
suffix = ""

mlist = FBModelList()
FBGetSelectedModels(mlist)

if len(mlist) == 0:
    FBMessageBox("Caution", "You must select some models", "OK")

else:
    check = FBMessageBox("Message", "Which to omit ?", "prefix", "suffix")

    if check == 1:
        prefix = FBMessageBoxGetUserValue("Message", "input prefix to omit", None,
                                        FBPopupInputType.kFBPopupString, "execute")
    else:
        suffix = FBMessageBoxGetUserValue("Message", "input suffix to omit", None,  
                                        FBPopupInputType.kFBPopupString, "execute")

    for model in mlist:
        if prefix:
            if model.Name.startswith(prefix[1]):
                model.Name = model.Name.replace(prefix[1], "").strip()
        elif suffix:
            if model.Name.endswith(suffix[1]):
                model.Name = model.Name.replace(suffix[1], "").strip()

# Cleanup
del(FBModelList, FBGetSelectedModels, FBMessageBox,
    FBMessageBoxGetUserValue, FBPopupInputType)

del(mlist, check, prefix, suffix, model)