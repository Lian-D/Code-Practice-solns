// Runtime: 96 ms, faster than 26.05% of TypeScript online submissions for Majority Element.
//     Memory Usage: 42.6 MB, less than 36.97% of TypeScript online submissions for Majority Element.

function majorityElement(nums: number[]): number {
    let numberHash: Map<number, number> = new Map();
    for (let i = 0; i < nums.length; i++) {
        let key = nums[i];
        if (numberHash.get(key) === undefined) {
            numberHash.set(key, 1);
        } else {
            let val = numberHash.get(key);
            numberHash.set(key, val+1);
        }
    }
    let retKey;
    let retVal = -1;
    Array.from(numberHash.keys()).forEach((key) => {
        let val = numberHash.get(key);
        if (val > retVal) {
            retVal = val;
            retKey = key;
        }
    });
    return retKey;
};