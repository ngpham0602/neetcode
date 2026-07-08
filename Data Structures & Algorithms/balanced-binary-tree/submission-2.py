# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, node):
        if node is None:
            return 0 
        left = self.height(node.left)
        right = self.height(node.right)
        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        total = 1 + max(left, right)
        diff = abs(self.height(root.left) - self.height(root.right))
        if diff > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        