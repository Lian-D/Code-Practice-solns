class Solution(object):
    def isValid(self, s):
        if len(s) == 0:
            return True
        if (len(s) % 2 != 0):
            return False
        stringStack = []
        
        for char in s:
            if (char in ['(', '{', '[']):
                stringStack.append(char)
            else:
                if len(stringStack) == 0 or stringStack.pop() != self.getCompletement(self, char):
                    return False
        if (len(stringStack) == 0): 
            return True    
        else: 
            return False
    
    def getCompletement(self, s):
        if s == ')':
            return '('
        elif s ==']':
            return '['
        elif s == '}':
            return '{'
        
solution = Solution
print(solution.isValid(solution,'')) #True
print(solution.isValid(solution,'(')) #False
print(solution.isValid(solution,'()')) #True
print(solution.isValid(solution,'[()]'))#True
print(solution.isValid(solution,'[[)]')) #False
print(solution.isValid(solution,'"()[]{}"')) #False
print(solution.isValid(solution,'((')) #False