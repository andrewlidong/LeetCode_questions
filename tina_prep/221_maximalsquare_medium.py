class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # input validation check
        if matrix is None or len(matrix) < 1:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        # initialize a dp grid with one additional column and one additional row to facilitate the index dp[row - 1][col] dp[row][col - 1] and dp[row - 1][col - 1] for cells in the first row and first column in matrix
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        max_side = 0

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    # be careful of indexing since the dp grid has an additional row and col
                    dp[r + 1][c + 1] = min(dp[r][c],
                                           dp[r + 1][c], dp[r][c + 1]) + 1
                    max_side = max(max_side, dp[r + 1][c + 1])

        return max_side * max_side

# Time: O(MN) where M is the row length and N is the col length, since we pass through every element in row * col
# Space: O(MN) because we create an additional dp grid (though we could optimize the solution to not keep track of the whole dp grid as we progress down the rows in matrix)


# try iterating through each element of the matrix, and once we run into a one, call a helper method to figure out the size of the square, and store the max size.
# helper method to figure out size of square could be growing right and down in equal proportions?
