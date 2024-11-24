class Solution(object):
    def largestUniqueNumber(self, s): 
        numHash = {}
        currLargest = -1
        for val in s:
            if val not in numHash:
                numHash[val] = 1
            else:
                numHash[val] += 1
        for val in s:
            if numHash[val] == 1:
                currLargest = max(currLargest, val)
        return currLargest

    
solution = Solution
print(solution.largestUniqueNumber(solution, [1,2,3,4,5])) #5
print(solution.largestUniqueNumber(solution, [1,1,2,2])) #-1
print(solution.largestUniqueNumber(solution, [9,3,5,1])) #9
print(solution.largestUniqueNumber(solution, [9,9,8,7])) #8