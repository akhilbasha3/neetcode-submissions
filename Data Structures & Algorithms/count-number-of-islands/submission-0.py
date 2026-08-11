class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        noofislands = 0
        visited = set()

        def island(i, j):
            if  i < 0 or j < 0 or i>= len(grid) or j>= len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            island(i-1,j)
            island(i,j-1)
            island(i+1,j)
            island(i,j+1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    noofislands += 1
                    island(row,col)

        return noofislands