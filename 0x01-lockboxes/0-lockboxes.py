#!/usr/bin/python3
""" Checks if all the boxes in a list can be unlocked. """


def canUnlockAll(boxes):
    """ LockBoxes Function """
    box = []
    for i in range(1, len(boxes)):
        order = [box.extend(x) for x in boxes[:i] + boxes[i + 1:]]
        if i in box:
            box = []
        else:
            return False
    return True
