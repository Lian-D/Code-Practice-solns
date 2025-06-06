# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if ((p is None and q is not None) or (q is None and p is not None)):
            return False
        if (p.val == q.val):
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        return False