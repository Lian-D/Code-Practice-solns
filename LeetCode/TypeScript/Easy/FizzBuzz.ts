// Runtime: 96 ms, faster than 14.59% of TypeScript online submissions for Fizz Buzz.
//     Memory Usage: 40.9 MB, less than 65.95% of TypeScript online submissions for Fizz Buzz.
function fizzBuzz(n: number): string[] {
    let ret: string[] = [];
    for (let i = 1; i <= n; i++) {
        if ((i % 3 === 0) && (i % 5 === 0)){
            ret.push("FizzBuzz");
        } else if(i % 3 === 0) {
            ret.push("Fizz");
        } else if ( i % 5 === 0) {
            ret.push("Buzz");
        } else {
            ret.push(i.toString());
        }
    }
    return ret;
};