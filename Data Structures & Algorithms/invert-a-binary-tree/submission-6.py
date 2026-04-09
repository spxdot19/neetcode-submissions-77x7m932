# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        # if root.left == None and root.right == None or root.val == 0:
        #     return root
        tmpL = root.left
        tmpR = root.right

        root.right =  tmpL
        root.left = tmpR

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
        