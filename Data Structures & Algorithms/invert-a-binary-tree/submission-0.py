# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  # Handle the case where the tree is empty

        queue = deque([root])

        while queue:
            nodes_in_current_level = len(queue)

            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                
                # Swap the left and right children of the current node
                node.left, node.right = node.right, node.left

                # Put the next level onto the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
           
        