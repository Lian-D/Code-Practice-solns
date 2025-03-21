class Solution(object):
    def longestPalindrome(self, s):
        stringHash = {}
        ret = 0
        for char in s:
            if not stringHash.get(char):
                stringHash[char] = 1
            else:
                stringHash[char] += 1
            if stringHash.get(char) % 2 == 0:
                ret += 2 
                del stringHash[char]
        for key in stringHash.keys():
            if stringHash.get(key) % 2 == 1:
                ret += 1
                break
        del stringHash
        return ret

solution = Solution()
print(solution.longestPalindrome("abcccba"))
print(solution.longestPalindrome("abcdba"))
print(solution.longestPalindrome("abcdEba"))
print(solution.longestPalindrome("abcdEAB"))
            

        