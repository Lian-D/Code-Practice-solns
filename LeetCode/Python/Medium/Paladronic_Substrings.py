class Solution(object):
    def countSubstrings(self, s):
        palidroneCount = 0
        for i in range(len(s)):
            palidroneCount += 1
            left, right = i - 1, i + 1
            while (left >= 0 and right < len(s)):
                if (s[left] == s[right]):
                    palidroneCount += 1
                    left -= 1
                    right += 1
                else:
                    break
        for i in range(len(s)):
            left = i
            right = i + 1
            while  (left >= 0 and right < len(s)):
                if (s[left] == s[right]):
                    palidroneCount += 1
                    left -= 1
                    right += 1
                else: 
                    break
        return palidroneCount

solution = Solution()
solution.countSubstrings('AAA')
solution.countSubstrings('ABC')

                
            