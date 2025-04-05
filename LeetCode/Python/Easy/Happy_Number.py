class Solution(object):
    def isHappy(self, n):
        if (n == 1 or n == 7):
            return True
        elif (n < 10):
            return False
        sum = 0
        while(n > 0):
            val = n%10
            sum += val*val
            n = n // 10
        return self.isHappy(sum)
            
solution = Solution()
print(solution.isHappy(19))
print(solution.isHappy(2))
print(solution.isHappy(111))
print(solution.isHappy(7))