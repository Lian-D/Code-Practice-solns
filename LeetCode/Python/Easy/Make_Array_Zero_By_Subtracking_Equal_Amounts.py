class Solution(object):
    def minimumOperations(self, nums):
        nums.sort() # 0, 1, 3, 5, 5
        val = 0
        steps = 0
        for i in nums:
            i -= val
            if i > 0:
                val += i
                steps += 1
        return steps
        
        
        
        
solution = Solution()
print(solution.minimumOperations([1,5,0,3,5]))