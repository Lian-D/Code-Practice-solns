class Solution(object):
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
        
        
solution = Solution()
print(solution.minCostClimbingStairs([10,15,20]))
print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(solution.minCostClimbingStairs([1,2,2,1,1,2]))