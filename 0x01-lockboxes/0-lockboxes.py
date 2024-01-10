#!/usr/bin/python3
"""
Checks if all the boxes in a list can be unlocked.
"""

def canUnlockAll(boxes):
    """This function takes a list of lists as argument
        and every list presents a box containing keys
        that can open other boxes
        and it returns true if all the boxes
        can be opened and false otherwise"""

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
