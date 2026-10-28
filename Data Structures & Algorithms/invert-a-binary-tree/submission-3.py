# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        curr = root

        def invertchild(curr):
            if not curr:
                return 
            if curr.left and curr.right:
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
            elif curr.left:
                curr.right = curr.left
                curr.left = None
            elif curr.right:
                curr.left = curr.right
                curr.right = None
            if curr.left:
                invertchild(curr.left)
            if curr.right:
                invertchild(curr.right)
        invertchild(curr)
        return root