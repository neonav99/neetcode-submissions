# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node):
            if node == None:
                return 0
            left_Max = dfs(node.left)
            right_Max = dfs(node.right)
            left_Max = max(left_Max,0)
            right_Max = max(right_Max,0)
            res[0] = max(res[0], node.val + left_Max + right_Max)
            return node.val + max(left_Max,right_Max)
        dfs(root)
        return res[0]