#!/usr/bin/python3
"""
Checks if all the boxes in a list can be unlocked.
"""

def canUnlockAll(boxes):

    keys = {i: box for i, box in enumerate(boxes)}
    keysSet = {0}
    canOpen = True
    for key, value in keys.items():
        for val in value:
            if (val != key):
                keysSet.add(val)
    for key, value in keys.items():
        if (key not in keysSet):
            canOpen = False
    return canOpen
