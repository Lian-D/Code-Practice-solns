// Runtime: 72 ms, faster than 97.59% of TypeScript online submissions for Two Sum.
// Memory Usage: 39.5 MB, less than 50.18% of TypeScript online submissions for Two Sum.

function twoSum(nums: number[], target: number): number[] {
    let numberHash: Map<number, number> = new Map()
    for (let i = 0; i < nums.length; i++) {
        let curr = nums[i]
        let compliment:number = target - curr;

        if (numberHash.get(compliment) !== undefined) {
            return [numberHash.get(compliment),i]
        }
        numberHash.set(curr, i);
    }
    return null;
}
