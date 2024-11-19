class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        totalSum = (n*(n+1))/2
        actualSum = 0
        for i in range(n):
            actualSum += nums[i]
        return totalSum - actualSum
    
solution = Solution           
print(solution.missingNumber(solution, [3,0,1]))     