from pyfbsdk import*

def checkExistingGroup():
    for cha in FBSystem().Scene.Characters:
        for grp in FBSystem().Scene.Groups:
            if grp.Name in (cha.Name + "/Skeleton", cha.Name + "/Mesh"):
                FBMessageBox("Caution","Some group might already exists...","OK")
                return True  
    else:
        return False

def SkeletonGroup(chara:FBCharacter, option = None):
    slist = FBModelList()
    for prop in chara.PropertyList:
        if prop.Name.endswith("Link") and len(prop) > 0:
            slist.append(prop[0])
    if option == None:
        return slist 
    if option == "g":
        groupname = chara.Name + "/Skeleton"
        group = FBGroup(groupname)
        for model in slist:
            group.ConnectSrc(model)

def MeshGroup(chara:FBCharacter, option = None):
    meshList = FBModelList()
    chara.GetSkinModelList(meshList) 
    if option == None:
        return meshList
    if option == "g":
        groupname = chara.Name + "/Mesh" 
        group = FBGroup(groupname)
        for mesh in meshList:
            group.ConnectSrc(mesh)

def BoneNum(chara:FBCharacter) -> int:
    returnNum = 0
    for prop in chara.PropertyList:
        if prop.Name.endswith("Link") and len(prop) > 0:
            returnNum += 1
    return returnNum

def isSetReference(chara:FBCharacter) -> bool:
    prop = chara.PropertyList.Find("ReferenceLink")
    if len(prop) > 0:
        return True
    else:
        return False

def ShapeKey(chara:FBCharacter, option):
    ShapeKeyList = list()
    meshList = FBModelList()
    chara.GetSkinModelList(meshList)
    count = 0
    for mesh in meshList:
        geo = mesh.Geometry
        for i in range(geo.ShapeGetCount()):
            name = geo.ShapeGetName(i)
            if not name in ShapeKeyList:
                ShapeKeyList.append(name)
            else:
                count += 1

    if option == "Num":
        return len(ShapeKeyList)
    
    if option == "InMultipleModel":
        if count > 1: 
            return True
        else:
            return False
        

def main():
    chara = FBApplication().CurrentCharacter
    if chara is None:
        FBMessageBox("Cauton", "Error : Select a Charater", "OK")
        del(chara)
    else:
        try:
            BoneNumResult = str(BoneNum(chara))
            ShapeNumResult = str(ShapeKey(chara,"Num"))
            multiResult = "No"
            if ShapeKey(chara, "InMultipleModel"): multiResult = "Yes"
            refResult = "No"
            if isSetReference(chara): refResult = "Yes"

            FBMessageBox("Result", 
                        "Bone number : " + BoneNumResult + "\n" \
                        + "ShapeKey number : " + ShapeNumResult + "\n" \
                        + "ShapeKey in Muletiple Model : " + multiResult + "\n" \
                        + "Reference : " + refResult,
                        "OK")

            if not checkExistingGroup():
                SkeletonGroup(chara, "g")
                MeshGroup(chara, "g")
                FBMessageBox("Result",
                                "These two groups created." + "\n\n" + \
                                " - " + FBSystem().Scene.Groups[-1].Name + "\n" + \
                                " - " + FBSystem().Scene.Groups[-2].Name + "\n\n" + \
                                "Check them in Resources Window >> Groups","OK")

        except Exception as err:
            FBMessageBox("caution", "An Error Occurred : {}".format(err), "OK") 

        finally:
            del(chara, BoneNumResult, ShapeNumResult, multiResult, refResult)


if __name__ in ("__main__", "builtins"):
   main()