# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preIdx = 0
        self.postIdx = 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        return self.__construct_tree(preorder, postorder)

    def __construct_tree(self,preorder, postorder):
        
        root = TreeNode(preorder[self.preIdx])
        self.preIdx+=1
        #concept - preorder = Root -> left/right, postorder = left/right -> root
        # this means when preorder and postorder point to the same element => that node doesnot have any more children
        # this is the only case when we return the node otherwise it has a sibling
        # the post order is the guardrail the prevents you from spinning up more children 
        if root.val != postorder[self.postIdx]:
            root.left = self.__construct_tree(preorder, postorder)

        if root.val != postorder[self.postIdx]:
            root.right = self.__construct_tree(preorder, postorder)

        self.postIdx+=1
        return root