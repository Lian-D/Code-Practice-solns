function singleNumber(nums: number[]): number {
    let numberHash: Map<number, number> = new Map();
    nums.forEach( (value):void => {
        if (numberHash.get(value) === undefined) {
            numberHash.set(value, 1);
        } else {
            let currValue = numberHash.get(value);
            numberHash.set(value, currValue+1);
        }
    });
    for (let i = 0; i < nums.length; i++) {
        if (numberHash.get(nums[i]) === 1) {
            return nums[i];
        }
    }
};