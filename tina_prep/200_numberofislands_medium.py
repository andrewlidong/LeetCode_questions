class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # validate input
        if not grid:
            return 0

        # define row, col and islandCount to return
        row = len(grid)
        col = len(grid[0])
        islandCount = 0

        # iterate through each element in the matrix
        for i in range(row):
            for j in range(col):
                # if we see a 1, perform a dfs (greedy) search which we leave to a helper function
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    # make sure to increment islandCount
                    islandCount += 1
        # return islandCount
        return islandCount

    def dfs(self, grid, i, j):
        # perform validation checks before making recursive calls
        # specifically search for more 1s, otherwise eagerly return out of helper function
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        # cross off visited points with an X (a bit cleaner than turning them into 0s)
        grid[i][j] = 'X'
        # grow across the coordinate plane
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

# time complexity O(M * N) where M and N are the rows and columns lengths of the grid
# space complexity O(M * N) where M and N are the rows and column lengths of the grid since we are modifying the grid.  To get around this we can slice (create a copy of the grid)


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # default check to validate input
#         if not grid:
#             return 0

#         height = len(grid)
#         width = len(grid[0])
#         islandCount = 0

#         for i in range(height):
#             for j in range(width):
#                 if grid[i][j] == "0":
#                     continue
#                 else:
#                     # make sure to only add 1 to islandCount
#                     islandCount += 1

#                     # initialize a stack to depth first search the lands every time we find an island
#                     stack = list()
#                     stack.append([i,j])

#                     # visit each '1' in the adjacent area with the stack
#                     while len(stack):
#                         [p, q] = stack.pop()

#                         if p >= 1 and grid[p - 1][q] == "1":
#                             stack.append([p - 1, q])

#                         if p < (height -1 ) and grid[p - 1][q] == "1":
#                             stack.append([p + 1, q])

#                         if q >= 1 and grid[p][q - 1] == "1":
#                             stack.append([p, q - 1])

#                         if q < width - 1 and grid[p][q + 1] == "1":
#                             stack.append([p, q + 1])

#                         # mark as visited
#                         grid[p][q] = "0"

#         return islandCount


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # default check to validate input
#         if not grid:
#             return 0

#         height = len(grid)
#         width = len(grid[0])
#         islandCount = 0

#         for i in range(height):
#             for j in range(width):
#                 traverseIsland(i, j, grid, islandCount)

#     def traverseIsland(self, x, y, grid, islandCount):
#         if grid[x][y] == "0":
#             continue
#         else:
#             #sum up only once per chance of meeting '1'
#             islandCount += 1
#             stack =


#         if grid[x][y] == "1":
#             if grid[x + 1][y]:
#                 grid[x][y] == "x"
#                 traverseIsland(x + 1, y, grid, islandCount)
#             if grid[x - 1][y]:
#                 grid[x][y] == "x"
#                 traverseIsland(x - 1, y, grid, islandCount)
#             if grid[x + 1][y]:
#                 grid[x][y] == "x"
#                 traverseIsland(x + 1, y, grid, islandCount)
#             if grid[x + 1][y]:
#                 grid[x][y] == "x"
#                 traverseIsland(x + 1, y, grid, islandCount)


# Save the length and width of the grid
# Be careful not to get an out of bounds error on the edges
# DRY out code by using a helper to create the traversal
# Apply a greedy algorithm, starting from the top left and crossing out if something is a visited island, maybe making it an x, seeing how long it goes.
# Skip already visited points, xs, and add the island to the island count when we've run out of 1s to visit from it
# Do this until we reach the end of the array.
