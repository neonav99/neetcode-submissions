# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value = []
        def dfs(node):
            if node == None:
                return 0
            if node.left:
                dfs(node.left)
            if node.val == None:
                value.append(None)
            value.append(node.val)
            if node.right:    
                dfs(node.right)
        dfs(root)
        print(value.sort)
        return value[k-1]