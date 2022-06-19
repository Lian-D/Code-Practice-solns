//Runtime: 93 ms, faster than 60.06% of TypeScript online submissions for Running Sum of 1d Array.
//Memory Usage: 44.2 MB, less than 91.06% of TypeScript online submissions for Running Sum of 1d Array.

function runningSum(nums: number[]): number[] {
    for (let i = 1; i < nums.length; i++) {
        let prev = i-1;
        nums[i] = nums[prev]+nums[i];
    }
    return nums;
};
