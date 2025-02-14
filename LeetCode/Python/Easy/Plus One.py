class Solution(object):
    def plusOne(self, digits):
        carry = 0
        for i in range(0, len(digits)):
            #print(i)
            carry = 0
            index = len(digits)-1-i
            if index is len(digits)-1:
                digits[index] = digits[index]+1
            value = digits[index]
            if(value >= 10 and index == 0):
                digits[index] = value % 10
                digits.insert(0,1)
            elif (value >= 10):
                digits[index] = value % 10
                digits[index-1] += 1 + carry
                carry = 1
        return digits


solution = Solution
solution.plusOne(solution,[1,2,3,4])  
solution.plusOne(solution,[9,9,9,9])  