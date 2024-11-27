class Solution(object):
    def containsDuplicate(self, nums):
        numberHash = {}
        for num in nums:
            if numberHash.get(num) != None:
                numberHash[num] += 1
            else:
                numberHash[num] = 1
        for value in numberHash:
            if numberHash.get(value) >= 2:
                return True
        return False 