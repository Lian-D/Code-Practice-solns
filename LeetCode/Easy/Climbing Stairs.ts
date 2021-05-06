// Runtime: 84 ms, faster than 41.80% of TypeScript online submissions for Climbing Stairs.
//     Memory Usage: 39.1 MB, less than 50.15% of TypeScript online submissions for Climbing Stairs.

function climbStairs(n: number): number {
    let nHash: Map<number, number> = new Map();
    nHash.set(1, 1);
    nHash.set(2,2);
    for (let i = 3; i <= n; i++) {
        let val:number = nHash.get(i-1) + nHash.get(i-2);
        nHash.set(i, val);
    }
    return nHash.get(n);
};