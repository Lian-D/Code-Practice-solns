class Solution(object):
    def isPalindrome(self, s):
        s = "".join(char for char in s if char.isalnum()).lower()
        stringStack = []
        for i in range(0, len(s)//2):
            stringStack.append(s[i])
        print(stringStack)
        for i in range(-(len(s)// -2), len(s)):
            if (s[i]) != stringStack.pop():
                return False
        return True
            
        

solution = Solution
print(solution.isPalindrome(solution, "A man, a plan, a canal: Panama")) #true
print(solution.isPalindrome(solution, "abba")) #true
print(solution.isPalindrome(solution, "false")) #false
print(solution.isPalindrome(solution, "ababa")) #true
print(solution.isPalindrome(solution, "")) #true