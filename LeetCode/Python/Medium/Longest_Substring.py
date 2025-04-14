class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        currLongest = 0
        lastSeenStringHash = {}
        while right < len(s):
            currChar = s[right]
            if (lastSeenStringHash.get(currChar) != None and lastSeenStringHash[currChar] >= left):
                left = lastSeenStringHash.get(currChar) + 1
            currLongest = max(currLongest, right - left + 1)
            lastSeenStringHash[currChar] = right
            right += 1
        return currLongest
    

solution = Solution()
print(solution.lengthOfLongestSubstring("AABCBCBB"))
print(solution.lengthOfLongestSubstring("BBBBB"))
print(solution.lengthOfLongestSubstring("PWWKEW"))
print(solution.lengthOfLongestSubstring("ABCDDDCBA"))
print(solution.lengthOfLongestSubstring("abba"))
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("ABabcABCD"))

            
            
        
        
        
        