# Create Custom HUD to show 60 fps frame value

from pyfbsdk import (FBPlayerControl, FBTimeMode, FBHUD, FBHUDTextElement,
                     FBHUDElementHAlignment, FBHUDElementVAlignment, FBSystem,
                     FBPropertyType, FBConstraintRelation, FBAnimationNode, FBConnect)

# Set Transport fps 60
lPlayer = FBPlayerControl()
lPlayer.SetTransportFps(FBTimeMode.kFBTimeMode60Frames)

# configure text hud element
lHud = FBHUD("CustomHUD")
lHud_frames = FBHUDTextElement("Previs_frames")
lHud_frames.Content = "frame in 60 fps : "
lHud_frames.X = 0
lHud_frames.Y = 0
lHud_frames.Height = 7
lHud_frames.Justification = FBHUDElementHAlignment.kFBHUDRight
lHud_frames.HorizontalDock = FBHUDElementHAlignment.kFBHUDRight
lHud_frames.VerticalDock = FBHUDElementVAlignment.kFBHUDTop
lHud.ConnectSrc(lHud_frames)

# set HUD to the current camera
renderer = FBSystem().Scene.Renderer
ActivePaneIndex = renderer.GetSelectedPaneIndex()
renderer.GetCameraInPane(ActivePaneIndex).ConnectSrc(lHud)

# create custom property
customprop = lHud.PropertyCreate("test prop", FBPropertyType.kFBPT_double, "Number", True, True, None)

# Animate custom property
customprop.SetAnimated(True)

# create property referece in the Text HUD element
lHud_frames.PropertyAddReferenceProperty(customprop)

# create relation constraint
lConstraint = FBConstraintRelation("HUD configure")
srcbox = lConstraint.CreateFunctionBox("System", "Local Time")
timetosecbox = lConstraint.CreateFunctionBox("Converters", "Time to seconds")
multiplybox = lConstraint.CreateFunctionBox("Number", "Multiply (a x b)")
dstbox = lConstraint.ConstrainObject(lHud)

# get box node function
def FindAnimationNode( parentNode:FBAnimationNode, nodeName:str ) -> FBAnimationNode:
    lResult = None
    for lNode in parentNode.Nodes:
        if lNode.Name == nodeName:
            lResult = lNode
            break
    return lResult

# create relation boxes
srcboxOutput = FindAnimationNode(srcbox.AnimationNodeOutGet(), "Result")
timetosecboxInput = FindAnimationNode(timetosecbox.AnimationNodeInGet(), "Time")
timetosecboxOutput = FindAnimationNode(timetosecbox.AnimationNodeOutGet(), "Result")
multiplyInput_a = FindAnimationNode(multiplybox.AnimationNodeInGet(), "a")
multiplyInput_b = FindAnimationNode(multiplybox.AnimationNodeInGet(), "b")
multiplyOutput = FindAnimationNode(multiplybox.AnimationNodeOutGet(), "Result")
dstboxInput = FindAnimationNode(dstbox.AnimationNodeInGet(), customprop.Name)

# connect boxes
if(srcboxOutput and timetosecboxInput and timetosecboxOutput 
   and multiplyInput_a and multiplyInput_b and multiplyOutput and dstboxInput):
    FBConnect(srcboxOutput, timetosecboxInput)
    FBConnect(timetosecboxOutput, multiplyInput_a)
    FBConnect(multiplyOutput, dstboxInput)

# set multiply box value
multiplyInput_b.WriteData([60.0])

# activate the constraint.
lConstraint.Active = True 

# cleanup
del(FBPlayerControl, FBTimeMode, FBHUD, FBHUDTextElement,
    FBHUDElementHAlignment, FBHUDElementVAlignment, FBSystem,
    FBPropertyType, FBConstraintRelation, FBAnimationNode, FBConnect)

del(lPlayer, lHud, lHud_frames, customprop, renderer, ActivePaneIndex, 
    lConstraint, srcbox, timetosecbox, multiplybox, dstbox, 
    srcboxOutput, timetosecboxInput, timetosecboxOutput,
    multiplyInput_a, multiplyInput_b, multiplyOutput, dstboxInput)

del(FindAnimationNode)