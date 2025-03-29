class Solution(object):
    def hammingWeight(self, n):
        ret = 0
        while n != 0:
            if n & 1 == 1:
                ret += 1
            n = n >> 1
        return ret
    

solution = Solution()
print(solution.hammingWeight(1)) # 1
print(solution.hammingWeight(5)) # 1
print(solution.hammingWeight(32)) # 1
print(solution.hammingWeight(2147483645)) # 1


            