# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.globalTopDiam = 0

        def depth(curr):
            if (curr == None):
                return 0
            
            left = depth(curr.left)
            right = depth(curr.right)

            self.globalTopDiam = max(self.globalTopDiam, left + right)
            return 1+max(left,right) 

        depth(root)
        return self.globalTopDiam
