import sys
from dataclasses import dataclass
from collections import deque
from typing import Optional


@dataclass
class Node:
    value: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None


def builder(values):
    if not values:
        return None

    root = Node(values[0])
    queue = deque([root])
    curr = 1

    while queue and curr < len(values):
        node = queue.popleft()

        if curr < len(values):
            left_val = values[curr]
            if node.value != 0 or (node.value == 0 and left_val == 0): #only make children of 0s if both parent and child are 0
                node.left = Node(left_val)
                queue.append(node.left)
            curr += 1

        if curr < len(values):
            right_val = values[curr]
            if node.value != 0 or (node.value == 0 and right_val == 0):
                node.right = Node(right_val)
                queue.append(node.right)
            curr += 1

    return root


def dfs(root, target):
    if not root or root.value == 0:
        return []

    stack = [(root, [root.value], root.value)]
    results = []

    while stack:
        node, path, total = stack.pop()

        if not node.left and not node.right and total == target:
            results.append(path)

        if node.right and (node.right.value != 0 or node.value == 0):
            stack.append((node.right, path + [node.right.value], total + node.right.value))
        if node.left and (node.left.value != 0 or node.value == 0):
            stack.append((node.left, path + [node.left.value], total + node.left.value))

    return results


def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    index = 0

    while index < len(lines):
        target = int(lines[index])
        tree = list(map(int, lines[index + 1].split()))
        root = builder(tree)

        results = dfs(root, target)

        for path in sorted(results):
            print(f"{target}: {', '.join(map(str, path))}")

        index += 2


if __name__ == '__main__':
    main()



