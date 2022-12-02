// Runtime: 144 ms, faster than 41.18% of TypeScript online submissions for Find All Numbers Disappeared in an Array.
//     Memory Usage: 57 MB, less than 5.15% of TypeScript online submissions for Find All Numbers Disappeared in an Array.
function findDisappearedNumbers(nums: number[]): number[] {
    let numberMap: Map<number, number> = new Map();
    for (let i = 0; i < nums.length; i++) {
        let key = nums[i];
        if (numberMap.get(key) === undefined) {
            numberMap.set(key, 1);
        } else {
            let val = numberMap.get(key);
            numberMap.set(key, val+1);
        }
    }
    let retArr: number[] = [];
    for (let i = 1; i <= nums.length; i++) {
        let key = i;
        if (numberMap.get(key) === undefined) {
            retArr.push(key);
        }
    }
    return retArr;
};