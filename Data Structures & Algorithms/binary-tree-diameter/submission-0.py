# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def depth(root):
            if root.left == None and root.right == None:
                return 0
            elif root.left == None:
                return depth(root.right) + 1
            elif root.right == None:
                return depth(root.left) + 1
            else:
                return max(depth(root.right), depth(root.left)) + 1

        
        if root.right == None and root.left == None:
            return 0
        elif root.right == None:
            return max(depth(root), self.diameterOfBinaryTree(root.left))
        elif root.left == None:
            return max(depth(root), self.diameterOfBinaryTree(root.right))
        else:
            return max(self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left), depth(root.right) + depth(root.left) + 2)

