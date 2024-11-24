class Solution(object):
    def firstUniqChar(self, s): 
        numberMap = {}
        for char in s:
            if numberMap.get(char):
                numberMap[char] = numberMap.get(char) + 1
            else:
                numberMap[char] = 1
        index = 0
        for char in s:
            check = numberMap.get(char)
            if check == 1:
                return index
            index += 1
        return -1
                

    
solution = Solution
print(solution.firstUniqChar(solution, "abbb")) #0
print(solution.firstUniqChar(solution, "abab")) #-1
print(solution.firstUniqChar(solution, "abcd")) #0
print(solution.firstUniqChar(solution, "ababcd")) #4