// Runtime: 84 ms, faster than 67.63% of TypeScript online submissions for Invert Binary Tree.
// Memory Usage: 40.3 MB, less than 48.20% of TypeScript online submissions for Invert Binary Tree.

class TreeNode {
        val: number
        left: TreeNode | null
        right: TreeNode | null
        constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
            this.val = (val === undefined ? 0 : val)
            this.left = (left === undefined ? null : left)
            this.right = (right === undefined ? null : right)

        }
}

function invertTree(root: TreeNode | null): TreeNode | null {
    if (root == null) {
        return root;
    }

    let newRight: TreeNode = invertTree(root.left);
    let newLeft: TreeNode  = invertTree(root.right);

    root.left = newLeft;
    root.right = newRight;

    return root;
};