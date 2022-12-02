// Runtime: 108 ms, faster than 91.57% of TypeScript online submissions for Merge Two Binary Trees.
//     Memory Usage: 46.2 MB, less than 91.57% of TypeScript online submissions for Merge Two Binary Trees.

function mergeTrees(root1: TreeNode | null, root2: TreeNode | null): TreeNode | null {
    if (!root1) {
        return root2;
    } else if (!root2) {
        return root1;
    }

    root1.val += root2.val;
    root1.left = mergeTrees(root1.left, root2.left);
    root1.right = mergeTrees(root1.right, root2.right);
    return root1;
};