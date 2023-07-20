#!/usr/bin/python3
""" Can all Lockboxes be unlocked """

def canUnlockAll(boxes):
    """ returns true if all boxes can be unlocked
        key will have to be same number as a box to
        unlock the box and box[0] is already unlocked
    """
    canUnlockAll = False
    boxKeys = {0: True}
    numberOfBoxes = len(boxes)
    while(True):

        numberOfKeys = len(boxKeys)

        for i in range(len(boxes)):
            if boxes[i] and boxKeys.get(i, False):
                for j in boxes[i]:
                    if j < numberOfBoxes:
                        boxKeys[j] = True
                    boxes[i] = None

        if not(len(boxKeys) > numberOfKeys):
            break

    if numberOfKeys == len(boxes):
        canUnlockAll = True

    return canUnlockAll
