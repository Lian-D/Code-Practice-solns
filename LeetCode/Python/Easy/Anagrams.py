class Solution(object):
    def isAnagram(self, s, t):
        stringHash = {}
        for char in s:
            if stringHash.get(char):
                stringHash[char] += 1
            else:
                stringHash[char] = 1
        for char in t:
            if stringHash.get(char) == 1:
                del stringHash[char]
            elif stringHash.get(char):
                stringHash[char] -= 1
            else:
                return False
        return stringHash == {}
        

solution = Solution
print(solution.isAnagram(solution, "banana", "ananab")) #true
print(solution.isAnagram(solution, "abba", "bbaa")) #true
print(solution.isAnagram(solution, "false", "true")) #true
print(solution.isAnagram(solution, "false", "tru")) #true