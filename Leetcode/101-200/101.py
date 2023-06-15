# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return check(a.left, b.right) and check(a.right, b.left)

        if root.left and root.right:
            return check(root.left, root.right)
        if not root.left and not root.right:
            return True
        return False