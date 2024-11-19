class Solution(object):
    def sumZero(self, n):
        end = []
        if n % 2 == 0:
            index = n/2
            for i in range(index):
                end.append(i+1)
                end.append(-abs(i+1))
            return end
        else:
            index = n//2
            for i in range(index):
                end.append(i+1)
                end.append(-abs(i+1))
            end.append(0)
            return end

solution = Solution
print(solution.sumZero(solution, 5))