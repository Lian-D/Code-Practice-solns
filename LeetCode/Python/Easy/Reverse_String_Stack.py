class Solution(object):
    def reverseString(self, s):
        stringStack = []
        for char in s:
            stringStack.append(char)
        s = ""
        while len(stringStack) != 0:
            s += stringStack.pop()
        return s