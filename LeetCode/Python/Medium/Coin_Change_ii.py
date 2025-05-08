class Solution(object):
    def change(self, amount, coins):
        table = {}  
        def dfs(coinIndex, accAmount):
            if accAmount == amount:
                return 1
            if accAmount > amount:
                return 0
            if coinIndex == len(coins):
                return 0
            if (coinIndex, accAmount) in table:
                return table[(coinIndex, accAmount)]
            
            table[(coinIndex, accAmount)] = dfs (coinIndex, accAmount + coins[coinIndex]) + dfs (coinIndex + 1, accAmount)
            return table[coinIndex, accAmount]
        return dfs(0,0)
    

solution = Solution()
print(solution.change(5, [1,2,5]))