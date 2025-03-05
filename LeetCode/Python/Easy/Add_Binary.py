class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        ret = ""
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            valA = int(a[i]) if i < len(a) else 0
            valB = int(b[i]) if i < len(b) else 0
            total = valA + valB + carry
            char = str(total % 2)
            carry = total // 2
            ret = char + ret
        if carry:
            ret = "1"+ret
        return ret

solution = Solution
print(solution.addBinary(solution, "11", "1"))
print(solution.addBinary(solution, "1010", "1011"))
print(solution.addBinary(solution, "0", "0"))