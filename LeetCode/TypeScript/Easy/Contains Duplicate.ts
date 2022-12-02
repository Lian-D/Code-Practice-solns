// Runtime: 76 ms, faster than 99.72% of TypeScript online submissions for Contains Duplicate.
//     Memory Usage: 44.9 MB, less than 49.86% of TypeScript online submissions for Contains Duplicate

function containsDuplicate(nums: number[]): boolean {
    let numberHash: Map<number,number> = new Map();

    for (let i: number = 0; i < nums.length; i++) {
        let num: number = nums[i];
        if (numberHash.get(num) != undefined) {
            return true;
        }
        numberHash.set(num, 1);
    }
    return false;
};