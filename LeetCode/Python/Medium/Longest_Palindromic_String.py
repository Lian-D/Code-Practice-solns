# class Solution(object):
#     def isPalidrome(self, s):
#         return s == s[::-1]
#     def longestPalindrome(self, s):
#         slow = 0
#         fast = 0
#         currLongest = []
#         curr = []    
#         while slow < len(s):
#             curr.append(s[fast])
#             if (self.isPalidrome(curr)):
#                 if (len(curr) > len(currLongest)):
#                     currLongest = curr.copy()
#             if (fast == len(s) - 1):
#                 slow += 1
#                 fast = slow
#                 curr = []
#             else: 
#                 fast += 1
#         return ''.join(currLongest)

class Solution(object):
    def longestPalindrome(self, s):
        result = ""
        resultLen = 0
        
        for i in range(len(s)):
            left, right = i, i
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1) > resultLen:
                    result = s[left:right+1] 
                    resultLen = right - left + 1
                left -= 1
                right += 1
            
        for i in range(len(s)):
            left, right = i, i+1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1) > resultLen:
                    result = s[left:right+1] 
                    resultLen = right - left + 1
                left -= 1
                right += 1
        return result
    
            
solution = Solution()
print(solution.longestPalindrome("ABABA"))
print(solution.longestPalindrome("CBAABAAC"))
            
            
    