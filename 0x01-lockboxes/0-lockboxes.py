#!/usr/bin/python3
"""
Checks if all the boxes in a list can be unlocked.
"""

def canUnlockAll(boxes):
    if not boxes or len(boxes) == 1:
        return True

    # Initiate keys, unlocked boxes, and track visited boxes
    keys = set(boxes[0])
    unlocked = {0}
    visited = set()

    while keys:

        new_keys = set()
        for box in unlocked - visited:
            for key in boxes[box]:
                if key not in unlocked:
                    new_keys.add(key)
                    unlocked.add(key)
            visited.add(box)

        if not new_keys:
            break

        keys |= new_keys

    return len(unlocked) == len(boxes)
