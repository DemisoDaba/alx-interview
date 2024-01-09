#!/usr/bin/python3
"""
Checks if all the boxes in a list can be unlocked.
"""

from collections import deque

def canUnlockAll(boxes_to_check):
    total_boxes = len(boxes_to_check)
    unlocked_boxes = [False] * total_boxes
    unlocked_boxes[0] = True
    queue = deque([0])
    
    while queue:
        current_box = queue.popleft()
        for key in boxes_to_check[current_box]:
            if key < total_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                queue.append(key)
                
    return all(unlocked_boxes)
