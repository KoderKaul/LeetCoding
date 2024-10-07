# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum=[-1001]
        def dfs(node):
            if not node:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            summ = node.val + l + r
            localMax=max(summ-l-r,summ-l,summ-r)
            maxSum[0]=max(maxSum[0],localMax,summ)
            return localMax
        dfs(root)
        return maxSum[0]