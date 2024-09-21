# -*- coding:utf-8 -*-

# シェイプキーの表示スクリプト


from pyfbsdk import*

# get character meshes
chara = FBApplication().CurrentCharacter

if chara:
    mlist = FBModelList()
    chara.GetSkinModelList(mlist)

    # initialize
    shapeNum_multicounted = 0           # duplicated shape count
    shapeNames_all = list()             # all shapes
    shapeNames_multicounted = list()    # shapes duplicated
    meshes_containsShape = list()       # meshes which have shapekeys
    display_all = ""                    # first result message

    # survey each mesh
    for mesh in mlist:
        geo = mesh.Geometry
        shapelist = []
        for i in range(geo.ShapeGetCount()):
            shapename = geo.ShapeGetName(i)
            shapelist.append(shapename)

            if shapename not in shapeNames_all:
                shapeNames_all.append(shapename)
            elif shapename not in shapeNames_multicounted:
                shapeNames_multicounted.append(shapename)
                shapeNum_multicounted += 1   
        
        if len(shapelist) > 0:
            meshes_containsShape.append(mesh.Name)
            formatted_mesh_name = "{:<25}".format(mesh.Name)
            formatted_shapes = ", ".join(shapelist)
            display_all += "   "                    \
                            + formatted_mesh_name   \
                            + " : "                 \
                            + formatted_shapes      \
                            +" \n"

    # display results
    FBMessageBox("Result", "{:<}".format("Shapekeys detected\n\n")
                            + display_all, "OK")

    # if duplication detected
    if shapeNum_multicounted > 0:
        display_duplicated = ""
        for name in shapeNames_multicounted:
            display_duplicated += name + ", "
        check = FBMessageBox("Caution", "CAUTION : The following shapekeys exists in the multiple meshes.\n\n"
                            + "   " + display_duplicated + "\n\n"
                            + "Do you want to make a mesh group ?",
                            "Yes",  # check == 1
                            "No"    # check == 2
                            )
        if check == 1:
            meshgroup = FBGroup("ShapedMeshes")
            for meshname in meshes_containsShape:
                meshmodel = FBFindModelByLabelName(meshname)
                if meshmodel:
                    meshgroup.ConnectSrc(meshmodel)

else:
    FBMessageBox("Caution", "Error : Select a Character.", "OK")