from pyfbsdk import*

def ApplyMirror()->None:
    chara = FBApplication().CurrentCharacter
    if not chara:
        FBMessageBox("Warning", "Error : No character selected", "OK")
        return

    # input keyword to specify right/left bone
    keyword_R_tuple = FBMessageBoxGetUserValue("Message", "keyword for RIGHT side bone ", None,
                                FBPopupInputType.kFBPopupString, "OK")
    keyword_L_tuple = FBMessageBoxGetUserValue("Message", "keyword for LEFT side bone ", None,
                            FBPopupInputType.kFBPopupString, "OK")
    
    keyword_R = keyword_R_tuple[1]
    keyword_L = keyword_L_tuple[1]

    # bone list for character skeleton
    charaModelList = FBModelList()
    RightBoneList = FBModelList()
    LeftBoneList  = FBModelList()

    for prop in chara.PropertyList:
        if(prop.Name.endswith("Link") and len(prop) > 0):
            charaModelList.append(prop[0])

    for bone in charaModelList:
        if keyword_R in bone.Name:
            RightBoneList.append(bone)
    if len(RightBoneList) == 0:
        FBMessageBox("Warning", f"Error : No bone found contains \"{keyword_R}\"")
        return

    for bone in charaModelList:
        if keyword_L in bone.Name:
            LeftBoneList.append(bone)            
    if len(LeftBoneList) == 0:
        FBMessageBox("Warning", f"Error : No bone found contains \"{keyword_L}\"")
        return

    # from which bone to apply the rotation
    whichsrc = FBMessageBox("Message", "Choose src to apply Rotation",
                            keyword_R, # whichsrc == 1
                            keyword_L, # whichsrc == 2
                            )
    
    # apply rotation
    target_list = zip(RightBoneList, LeftBoneList)
    if whichsrc == 1:
        for bone_R, bone_L in target_list:
            bone_L.Rotation = FBVector3d(bone_R.Rotation[0], -bone_R.Rotation[1], -bone_R.Rotation[2])
    else:
        for bone_R, bone_L in target_list:
            bone_R.Rotation = FBVector3d(bone_L.Rotation[0], -bone_L.Rotation[1], -bone_L.Rotation[2])


if __name__ in ("__main__", "builtins"):
    ApplyMirror()
    # Note : This tranformation is temporary