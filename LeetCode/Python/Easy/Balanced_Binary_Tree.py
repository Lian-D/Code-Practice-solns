# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        if root is None: return True
        self.balanced = True
        
        def countHeight(node):
            if node is None:
                return 0
            left = countHeight(node.left)
            right = countHeight(node.right)
            if (abs(left - right) > 1):
                self.balanced = False
            return max(left, right) + 1
        
        countHeight(root)
        return self.balanced 