class Solution(object):
    def numIslands(self, grid):
        numIsland = 0
        for y in range(len(grid)):
            for x in range (len(grid[0])):
                if grid[y][x] == "1":
                    numIsland += 1
                    self.floodIsland(grid, x, y)
        return numIsland
        

    def floodIsland(self, grid, x, y):
        if (x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] != "1"):
            return
        
        grid[y][x] = "0"  
        self.floodIsland(grid, x+1, y)
        self.floodIsland(grid, x, y+1)
        self.floodIsland(grid, x-1, y)
        self.floodIsland(grid, x, y-1)