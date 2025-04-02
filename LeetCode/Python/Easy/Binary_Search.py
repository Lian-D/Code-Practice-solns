class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while (left <= right):
            mid = right+left//2
            if (nums[mid] == target):
                return mid
            if (target > nums[mid]):
                left = mid+1
            else:
                right = mid-1
        return -1