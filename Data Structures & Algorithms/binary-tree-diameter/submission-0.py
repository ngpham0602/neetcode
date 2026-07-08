# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def length(node):
            if node is None:
                return 0
            self.diameter = max(self.diameter, (length(node.left) + length(node.right)))
            return 1 + max(length(node.left), length(node.right))
        
        length(root)
        return self.diameter
        
        