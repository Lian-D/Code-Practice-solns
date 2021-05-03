// Runtime: 96 ms, faster than 30.20% of TypeScript online submissions for Maximum Depth of Binary Tree.
// Memory Usage: 42.6 MB, less than 56.41% of TypeScript online submissions for Maximum Depth of Binary Tree.

function maxDepth(root: TreeNode | null): number {
    if (root == null){
        return 0;
    }
    return maxDepthHelper(root, 0);
};

function maxDepthHelper(root: TreeNode, depth: number) {
    if (root == null){
        return depth;
    }
    let right: number =  maxDepthHelper(root.right, depth+1);
    let left: number =  maxDepthHelper(root.left, depth+1);

    let val: number = (right > left) ? right : left;
    return val;
}