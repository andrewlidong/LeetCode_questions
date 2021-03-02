class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        n = len(nums)

        # dp will store the results of our calls
        dp = [[0] * n for _ in range(n)]

        # iterate over dp and incrementally build up to dp[0][n - 1]
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                # same formula to get the best score from (left, right)
                dp[left][right] = max(nums[left] * nums[i] * nums[right] +
                                      dp[left][i] + dp[i][right] for i in range(left + 1, right))

        return dp[0][n - 1]

# Find every possible order in which balloons can be burst.
# We can make a small improvement by caching the set of existing balloons
# Since each balloon can be burst or not be burst, we are incurring extra time, and are looking at a solution worse than O(2^N)
# Divide and Conquer
# After bursting balloon i, we can divide the problem into the balloons to the left of i and to the right of i.
# To find the optimal solution we check every optimal solution after bursting each balloon.
# Since we will find the optimal solution for every range in nums, and we burst every balloon in every range to find the optimal solution, we have an O(N^2) * O(N) = O(N^3) solution.
# If we try to divide
