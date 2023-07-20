def canUnlockAll(boxes):
    total_boxes = len(boxes)
    visited = set()
    stack = [0]  # Start from box 0 (the first box)

    while stack:
        box = stack.pop()
        visited.add(box)

        # Check all the keys in the current box
        for key in boxes[box]:
            # If the key opens a new box that hasn't been visited yet,
            # add it to the stack
            if key not in visited and 0 <= key < total_boxes:
                stack.append(key)

    # If all boxes have been visited, then all boxes can be opened
    return len(visited) == total_boxes
