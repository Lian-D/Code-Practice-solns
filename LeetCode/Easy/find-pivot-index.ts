//Runtime: 81 ms, faster than 92.91% of TypeScript online submissions for Find Pivot Index.
//Memory Usage: 45.6 MB, less than 31.50% of TypeScript online submissions for Find Pivot Index.

function pivotIndex(nums: number[]): number {
    let arrTotal = nums.reduce( (a,b) => { return a+b});
    let cumLeftVal = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i != 0) {
            cumLeftVal += nums[i-1];
        }
        if ((arrTotal - nums[i] - cumLeftVal) == cumLeftVal) {
            return i;
        }
    }
    return -1;
};
