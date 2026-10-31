# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {value:i for i, value in enumerate(inorder)}
        self.index = 0
        def solve(left, right):
            if left > right:
                return None
            
            val = preorder[self.index]
            self.index+=1

            root = TreeNode(val)
            mid = index_map[val]
            root.left = solve(left, mid-1)
            root.right = solve(mid+1, right)
            return root
        return solve(0, len(inorder) - 1)
            