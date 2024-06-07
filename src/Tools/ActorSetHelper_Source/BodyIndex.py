# -*- coding: utf-8 -*-

import pyfbsdk 
from pyfbsdk import*


MarkerSetIndex = {
    # for HipTracker
    "HipTracker"            : pyfbsdk.FBSkeletonNodeId.kFBSkeletonHipsIndex,

    # for LeftKnee/Foot Tracker
    "LeftKneeTracker"       : pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftKneeIndex,
    "LeftFootTracker"       : pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftAnkleIndex,

    # for RightKnee/Foot Tracker
    "RightKneeTracker"      : pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightKneeIndex,
    "RightFootTracker"      : pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightAnkleIndex,

    # for BodyTracker
    "BodyTracker"           : pyfbsdk.FBSkeletonNodeId.kFBSkeletonChestIndex,

    # for LeftShoulder/Elbow/Hand Tracker
    "LeftShoulderTracker"   : pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftCollarIndex,
    "LeftElbowTracker"      : pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftElbowIndex,
    "LeftHandTracker"       : pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftWristIndex,

    # for RightShoulder/Elbow/Hand Tracker
    "RightShoulderTracker"  : pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightCollarIndex,
    "RightElbowTracker"     : pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightElbowIndex,
    "RightHandTracker"      : pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightWristIndex,
    
    # for headTracker
    "headTracker": pyfbsdk.FBSkeletonNodeId.kFBSkeletonHeadIndex,
}


AllActorIndex = {
    0: pyfbsdk.FBSkeletonNodeId.kFBSkeletonHipsIndex,
    1: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftHipIndex,
    2: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftKneeIndex,
    3: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftAnkleIndex,
    4: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftFootIndex,
    5: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightHipIndex,
    6: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightKneeIndex,
    7: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightAnkleIndex,
    8: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightFootIndex,
    9: pyfbsdk.FBSkeletonNodeId.kFBSkeletonWaistIndex,
    10: pyfbsdk.FBSkeletonNodeId.kFBSkeletonChestIndex,
    11: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftCollarIndex,
    12: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftShoulderIndex,
    13: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftElbowIndex,
    14: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftWristIndex,
    15: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightCollarIndex,
    16: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightShoulderIndex,
    17: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightElbowIndex,
    18: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightWristIndex,
    19: pyfbsdk.FBSkeletonNodeId.kFBSkeletonNeckIndex,
    20: pyfbsdk.FBSkeletonNodeId.kFBSkeletonHeadIndex,
    21: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftThumbAIndex,
    22: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftThumbBIndex,
    23: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftThumbCIndex,
    24: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftIndexAIndex,
    25: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftIndexBIndex,
    26: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftIndexCIndex,
    27: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftMiddleAIndex,
    28: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftMiddleBIndex,
    29: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftMiddleCIndex,
    30: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftRingAIndex,
    31: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftRingBIndex,
    32: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftRingCIndex,
    33: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftPinkyAIndex,
    34: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftPinkyBIndex,
    35: pyfbsdk.FBSkeletonNodeId.kFBSkeletonLeftPinkyCIndex,
    36: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightThumbAIndex,
    37: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightThumbBIndex,
    38: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightThumbCIndex,
    39: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightIndexAIndex,
    40: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightIndexBIndex,
    41: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightIndexCIndex,
    42: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightMiddleAIndex,
    43: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightMiddleBIndex,
    44: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightMiddleCIndex,
    45: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightRingAIndex,
    46: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightRingBIndex,
    47: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightRingCIndex,
    48: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightPinkyAIndex,
    49: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightPinkyBIndex,
    50: pyfbsdk.FBSkeletonNodeId.kFBSkeletonRightPinkyCIndex,
}