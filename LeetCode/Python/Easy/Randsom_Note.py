class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        stringHash = {}
        for i in magazine:
            if stringHash.get(i):
                stringHash[i] += 1
            else: 
                stringHash[i] = 1
        for i in ransomNote:
            if stringHash.get(i):
                val = stringHash.get(i)
                if val > 1:
                    stringHash[i] -= 1
                elif val == 1:
                    del stringHash[i]
            else: return False
        return True


solution = Solution()
print(solution.canConstruct("abc", "abc"))
print(solution.canConstruct("abc", "aex"))
print(solution.canConstruct("abc", "ab"))
print(solution.canConstruct("abc", "abcc"))
print(solution.canConstruct("abcc", "abcc"))
