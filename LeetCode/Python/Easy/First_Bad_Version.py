# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if (version >= 4):
        return True
    else: 
        return False

class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        mid = right + (right - left) // 2
        while (left < right):
            mid = left + ((right - left) // 2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return mid
            
Solution = Solution()
print(Solution.firstBadVersion(5))
print(Solution.firstBadVersion(10))
        