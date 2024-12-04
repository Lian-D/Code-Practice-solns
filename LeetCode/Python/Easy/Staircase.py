class Solution(object):
    def climbStairs(self, n):
        if n <= 3: 
            return n
        else:
            memo = {}
            memo[1] = 1
            memo[2] = 2
            for i in range(3, n+1):
                memo[i] = memo.get(i-1) + memo.get(i-2)
        return memo[n]