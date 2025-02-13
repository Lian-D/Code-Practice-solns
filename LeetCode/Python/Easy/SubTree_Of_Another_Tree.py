# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sameTree(self, curr, subRootCurr):
        if (curr == None and subRootCurr == None):
            return True
        if (curr != None and subRootCurr != None and curr.val == subRootCurr.val):
            return (self.sameTree(curr.right, subRootCurr.right) and self.sameTree(curr.left, subRootCurr.left))
        return False
    def isSubtree(self, root, subRoot):   
        if(subRoot == None):
            return True
        if (root == None):
            return False
        if self.sameTree(root, subRoot):
            return True
        return ((
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)))

def test_subtree():
    # Test Case 1: Identical trees
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    
    sub1 = TreeNode(3)
    sub1.left = TreeNode(4)
    sub1.right = TreeNode(5)
    
    # Test Case 2: Subtree in larger tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    
    sub2 = TreeNode(3)
    sub2.left = TreeNode(4)
    sub2.right = TreeNode(5)
    
    # Test Case 3: Similar but not identical
    root3 = TreeNode(3)
    root3.left = TreeNode(4)
    root3.right = TreeNode(5)
    root3.left.left = TreeNode(1)
    
    sub3 = TreeNode(3)
    sub3.left = TreeNode(4)
    sub3.right = TreeNode(5)
    
    # Test Case 4: Empty subtree
    root4 = TreeNode(1)
    sub4 = None
    
    solution = Solution()
    
    tests = [
        (root1, sub1, True),  # Identical trees
        (root2, sub2, True),  # Valid subtree
        (root3, sub3, False), # Similar but not subtree
        (root4, sub4, True),  # Empty subtree
        (None, TreeNode(1), False)  # Empty main tree
    ]
    
    for i, (root, sub, expected) in enumerate(tests):
        result = solution.isSubtree(root, sub)
        print(f"Test {i+1}: {'PASS' if result == expected else 'FAIL'}")
        if result != expected:
            print(f"Expected {expected}, got {result}")

test_subtree()
