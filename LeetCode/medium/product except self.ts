// Runtime: 124 ms, faster than 66.00% of TypeScript online submissions for Product of Array Except Self.
//     Memory Usage: 49.8 MB, less than 44.00% of TypeScript online submissions for Product of Array Except Self.

function productExceptSelf(nums: number[]): number[] {
    let arrTotal:number = 1;
    let nonZeroArrTotal: number = 1;
    let zeroCounter: number = 0;
    let currArr = [];

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0 && !zeroCounter) {
            nonZeroArrTotal *= 1;
            arrTotal *= nums[i];
            zeroCounter++;
        } else {
            nonZeroArrTotal *= nums[i];
            arrTotal *= nums[i];
        }
    }
    for (let j = 0; j < nums.length; j++) {
        if (nums[j] === 0 && zeroCounter === 1) {
            currArr.push(nonZeroArrTotal);
        } else {
            currArr.push(arrTotal / nums[j]);
        }
    }
    return currArr;
}

console.log(productExceptSelf([1,2,0,4]));