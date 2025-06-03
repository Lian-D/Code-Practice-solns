class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        currMax = 0
        
        while (left < right):
            area = min(height[left], height[right]) * (right - left)
            if (area > currMax):
                currMax = area
            if (height[left] >= height[right]):
                right -= 1
            elif (height[right] > height[left]):
                left += 1
        return currMax
    
solution = Solution()
solution.maxArea([1,8,6,2,5,4,8,3,7])
solution.maxArea([1,8,1,8,1])
            
        