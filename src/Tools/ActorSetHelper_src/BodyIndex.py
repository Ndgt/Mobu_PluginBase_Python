# -*- coding: utf-8 -*-

from pyfbsdk import FBSkeletonNodeId

MarkerSetIndex = {
    # for HipTracker
    "HipTracker"            : FBSkeletonNodeId.kFBSkeletonHipsIndex,

    # for LeftKnee/Foot Tracker
    "LeftKneeTracker"       : FBSkeletonNodeId.kFBSkeletonLeftKneeIndex,
    "LeftFootTracker"       : FBSkeletonNodeId.kFBSkeletonLeftAnkleIndex,

    # for RightKnee/Foot Tracker
    "RightKneeTracker"      : FBSkeletonNodeId.kFBSkeletonRightKneeIndex,
    "RightFootTracker"      : FBSkeletonNodeId.kFBSkeletonRightAnkleIndex,

    # for BodyTracker
    "BodyTracker"           : FBSkeletonNodeId.kFBSkeletonChestIndex,

    # for LeftShoulder/Elbow/Hand Tracker
    "LeftShoulderTracker"   : FBSkeletonNodeId.kFBSkeletonLeftCollarIndex,
    "LeftElbowTracker"      : FBSkeletonNodeId.kFBSkeletonLeftElbowIndex,
    "LeftHandTracker"       : FBSkeletonNodeId.kFBSkeletonLeftWristIndex,

    # for RightShoulder/Elbow/Hand Tracker
    "RightShoulderTracker"  : FBSkeletonNodeId.kFBSkeletonRightCollarIndex,
    "RightElbowTracker"     : FBSkeletonNodeId.kFBSkeletonRightElbowIndex,
    "RightHandTracker"      : FBSkeletonNodeId.kFBSkeletonRightWristIndex,
    
    # for headTracker
    "HeadTracker": FBSkeletonNodeId.kFBSkeletonHeadIndex,
}


AllActorIndex = {
    0: FBSkeletonNodeId.kFBSkeletonHipsIndex,
    1: FBSkeletonNodeId.kFBSkeletonLeftHipIndex,
    2: FBSkeletonNodeId.kFBSkeletonLeftKneeIndex,
    3: FBSkeletonNodeId.kFBSkeletonLeftAnkleIndex,
    4: FBSkeletonNodeId.kFBSkeletonLeftFootIndex,
    5: FBSkeletonNodeId.kFBSkeletonRightHipIndex,
    6: FBSkeletonNodeId.kFBSkeletonRightKneeIndex,
    7: FBSkeletonNodeId.kFBSkeletonRightAnkleIndex,
    8: FBSkeletonNodeId.kFBSkeletonRightFootIndex,
    9: FBSkeletonNodeId.kFBSkeletonWaistIndex,
    10: FBSkeletonNodeId.kFBSkeletonChestIndex,
    11: FBSkeletonNodeId.kFBSkeletonLeftCollarIndex,
    12: FBSkeletonNodeId.kFBSkeletonLeftShoulderIndex,
    13: FBSkeletonNodeId.kFBSkeletonLeftElbowIndex,
    14: FBSkeletonNodeId.kFBSkeletonLeftWristIndex,
    15: FBSkeletonNodeId.kFBSkeletonRightCollarIndex,
    16: FBSkeletonNodeId.kFBSkeletonRightShoulderIndex,
    17: FBSkeletonNodeId.kFBSkeletonRightElbowIndex,
    18: FBSkeletonNodeId.kFBSkeletonRightWristIndex,
    19: FBSkeletonNodeId.kFBSkeletonNeckIndex,
    20: FBSkeletonNodeId.kFBSkeletonHeadIndex,
    21: FBSkeletonNodeId.kFBSkeletonLeftThumbAIndex,
    22: FBSkeletonNodeId.kFBSkeletonLeftThumbBIndex,
    23: FBSkeletonNodeId.kFBSkeletonLeftThumbCIndex,
    24: FBSkeletonNodeId.kFBSkeletonLeftIndexAIndex,
    25: FBSkeletonNodeId.kFBSkeletonLeftIndexBIndex,
    26: FBSkeletonNodeId.kFBSkeletonLeftIndexCIndex,
    27: FBSkeletonNodeId.kFBSkeletonLeftMiddleAIndex,
    28: FBSkeletonNodeId.kFBSkeletonLeftMiddleBIndex,
    29: FBSkeletonNodeId.kFBSkeletonLeftMiddleCIndex,
    30: FBSkeletonNodeId.kFBSkeletonLeftRingAIndex,
    31: FBSkeletonNodeId.kFBSkeletonLeftRingBIndex,
    32: FBSkeletonNodeId.kFBSkeletonLeftRingCIndex,
    33: FBSkeletonNodeId.kFBSkeletonLeftPinkyAIndex,
    34: FBSkeletonNodeId.kFBSkeletonLeftPinkyBIndex,
    35: FBSkeletonNodeId.kFBSkeletonLeftPinkyCIndex,
    36: FBSkeletonNodeId.kFBSkeletonRightThumbAIndex,
    37: FBSkeletonNodeId.kFBSkeletonRightThumbBIndex,
    38: FBSkeletonNodeId.kFBSkeletonRightThumbCIndex,
    39: FBSkeletonNodeId.kFBSkeletonRightIndexAIndex,
    40: FBSkeletonNodeId.kFBSkeletonRightIndexBIndex,
    41: FBSkeletonNodeId.kFBSkeletonRightIndexCIndex,
    42: FBSkeletonNodeId.kFBSkeletonRightMiddleAIndex,
    43: FBSkeletonNodeId.kFBSkeletonRightMiddleBIndex,
    44: FBSkeletonNodeId.kFBSkeletonRightMiddleCIndex,
    45: FBSkeletonNodeId.kFBSkeletonRightRingAIndex,
    46: FBSkeletonNodeId.kFBSkeletonRightRingBIndex,
    47: FBSkeletonNodeId.kFBSkeletonRightRingCIndex,
    48: FBSkeletonNodeId.kFBSkeletonRightPinkyAIndex,
    49: FBSkeletonNodeId.kFBSkeletonRightPinkyBIndex,
    50: FBSkeletonNodeId.kFBSkeletonRightPinkyCIndex,
}