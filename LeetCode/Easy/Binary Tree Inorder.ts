// Runtime: 68 ms, faster than 99.63% of TypeScript online submissions for Binary Tree Inorder Traversal.
//     Memory Usage: 40.4 MB, less than 30.37% of TypeScript online submissions for Binary Tree Inorder Traversal.

function inorderTraversal(root: TreeNode | null): number[] {
    if (root === null) {
        return [];
    } else {
        return [].concat(inorderTraversal(root.left)).concat([root.val]).concat(inorderTraversal(root.right));
    }
};