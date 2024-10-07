# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node,p,q):
            # print(node.val)
            if p.val <= node.val <= q.val:
                return node

            if q.val < node.val:
                return dfs(node.left,p,q)
            elif p.val>node.val:
                return dfs(node.right,p,q)

            if q.val==node.val:
                return q
            elif p.val==node.val:
                return p
        if p.val > q.val:
            return dfs(root,q,p)
        return dfs(root,p,q)

#         a
#     b       c
# d       e f     g