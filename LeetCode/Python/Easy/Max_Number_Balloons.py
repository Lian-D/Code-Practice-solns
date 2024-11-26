class Solution(object):
    def maxNumberOfBalloons(self, text):
        stringHash = {}
        text = text.lower()
        stringHash['b'] = 0
        stringHash['a'] = 0
        stringHash['l'] = 0
        stringHash['o'] = 0
        stringHash['n'] = 0
        for char in text:
            if char in stringHash:
                stringHash[char] += 1
        return min (stringHash['b'],
                    stringHash['a'],
                    stringHash['l']//2,
                    stringHash['o']//2,
                    stringHash['n'])

solution = Solution
print(solution.maxNumberOfBalloons(solution, "balloons")) 
print(solution.maxNumberOfBalloons(solution, "balloon")) 
print(solution.maxNumberOfBalloons(solution, "balloonsballoons")) 
print(solution.maxNumberOfBalloons(solution, "baloons")) 
print(solution.maxNumberOfBalloons(solution, "snoonlab")) 
print(solution.maxNumberOfBalloons(solution, "nlaebolko")) 