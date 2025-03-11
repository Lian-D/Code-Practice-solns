import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while(len(stones) > 1):
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)

            if (s1 != s2):
                heapq.heappush(stones, -(s1-s2))
        if (len(stones) >= 1):
            return -heapq.heappop(stones)
        else:
            return 0


solution = Solution
print(solution.lastStoneWeight(solution, [1,2,2,3]))    
print(solution.lastStoneWeight(solution, [2,7,4,1,8,1]))