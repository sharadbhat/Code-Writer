# Leetcode
# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [[root, 0]]
        depth = 0
        rightView = []

        while len(queue) > 0:
            curr, currDep = queue.pop(0)

            if depth == currDep:
                rightView.append(curr.val)
                depth += 1

            if curr.right:
                queue.append([curr.right, currDep + 1])

            if curr.left:
                queue.append([curr.left, currDep + 1])

        return rightView
