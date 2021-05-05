// Runtime: 108 ms, faster than 57.11% of TypeScript online submissions for Best Time to Buy and Sell Stock.
//     Memory Usage: 49.6 MB, less than 59.90% of TypeScript online submissions for Best Time to Buy and Sell Stock.

function maxProfit(prices: number[]): number {
    let minPrice:number = 9999;
    let maxProfit:number = 0;
    for (let i = 0; i< prices.length; i++) {
        let curr = prices[i];
        if (curr < minPrice) {
            minPrice = curr
        } else if (curr - minPrice > maxProfit) {
            maxProfit = curr - minPrice;
        }
    }
    return maxProfit;

};