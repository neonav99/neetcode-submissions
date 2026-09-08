# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if subRoot == None:
            return True
        
        if self.sameTree(root,subRoot):
            return True

        left_exp = self.isSubtree(root.left, subRoot)
        right_exp = self.isSubtree(root.right, subRoot)
        return left_exp or right_exp   

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:   
        if root == None and subRoot == None:
            return True
        if root and subRoot and root.val == subRoot.val:
            left = self.sameTree(root.left,subRoot.left)
            right = self.sameTree(root.right,subRoot.right)
            return left and right
        return False