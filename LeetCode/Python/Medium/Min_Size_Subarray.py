class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        sum = 0
        result = float('inf')

        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                result = min(result, right + 1 - left)
                print("leftIndex: "+str(left)+"rightIndex: "+str(right)+"sum: "+str(sum))
                sum -= nums[left]
                left += 1

        return result if result != float('inf') else 0



                 

solution = Solution
print(solution.minSubArrayLen(solution, 11,[1,1,1,1,1,1,1,1])) # 0
print(solution.minSubArrayLen(solution, 7, [2,3,1,2,4,3])) # 2
print(solution.minSubArrayLen(solution, 4, [1,4,4])) # 1
print(solution.minSubArrayLen(solution, 11,[11,1,3,4,5])) # 1 
print(solution.minSubArrayLen(solution, 11,[1,2,3,4,5])) #3