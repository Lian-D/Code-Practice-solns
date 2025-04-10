class Solution(object):
    def myAtoi(self, s):
        ret, neg = 0, 1
        s = s.strip()
        n = 0
        if s is '':
            return 0
        if s[0] == '-':
            neg = -1
            n = 1
        elif s[0] == '+':
            n = 1
            
        for i in range(n, len(s)):
            if (s[i].isdigit()):
                ret = ret*10 + int(s[i])
            else:
                break
            
        if neg*ret > 2**31 -1:
            return 2**31-1
        elif neg*ret < -2**31:
           return -2**31

        return ret*neg 
    
solution = Solution()
print(solution.myAtoi("42")) # 42
print(solution.myAtoi("-42")) # -42
print(solution.myAtoi("+42")) # 42
print(solution.myAtoi("+42ABC")) # 42
print(solution.myAtoi("words 987")) #0
print(solution.myAtoi("0-1")) # 0
print(solution.myAtoi("-91283472332")) # 0
print(solution.myAtoi("91283472333")) # 0
print(solution.myAtoi(" ")) # 0







            
        