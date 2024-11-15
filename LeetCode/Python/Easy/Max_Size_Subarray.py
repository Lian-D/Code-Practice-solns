class Solution(object):
    def maximumSubarraySum(self, nums, k):
        left = 0
        right = left + k
        currLargest = 0

        tempLeft = 0
        tempSum = 0

        # Case if K is larger than anticipated
        if (k > len(nums)):
            return 0
        
        # Calculate the intial sum of the first part of the window
        while(tempLeft < right) :
            tempSum = nums[tempLeft]+tempSum
            tempLeft += 1 
        currLargest = tempSum

        # Sliding Window,
        while (right < len(nums)):
            tempSum -= nums[left]
            tempSum += nums[right]

            if (tempSum >= currLargest):
                currLargest = tempSum
            
            left += 1
            right += 1
        
        return currLargest
    
solution = Solution
print(solution.maximumSubarraySum(solution, [1,1,1,4], 9))
print(solution.maximumSubarraySum(solution, [100, 200, 300, 400], 2))
print(solution.maximumSubarraySum(solution, [1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
print(solution.maximumSubarraySum(solution, [2, 3], 3))