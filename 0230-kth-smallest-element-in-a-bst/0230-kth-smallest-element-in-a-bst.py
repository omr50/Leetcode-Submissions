# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = []
        def dfs(root):
            if root:
                dfs(root.left)
                num.append(root.val)
                if len(num) == k:
                    return
                dfs(root.right)
        dfs(root)
        return num[k-1]