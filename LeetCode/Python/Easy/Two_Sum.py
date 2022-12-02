class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for x in range(len(nums)):
            compliment = target - nums[x]
            if (compliment in dict):
                return [dict.get(compliment), x]
            dict[nums[x]] = x


solution = Solution
print(solution.twoSum(solution, [3,2,4], 6))