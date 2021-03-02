# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         start, end, profit = zip(*sorted(zip(startTime, endTime, profit)))
#         jump = {i: bisect.bisect_left(start, end[i]) for i in range(len(start))}

#         def helper(i):
#             if i == len(start): return 0
#             return max(helper(i + 1), profit[i] + helper(jump[i]))

#         return helper(0)

# Time: O(nlogn) because bisect.bisect_left is a log(n) operation
# Space: O(n)

# input: 3 arrays, one with start times, one with end times, and one with profits for each job.
# output: max profits

# sort the elements by starting time, then define a dp array as the maximum profit taking elements from the suffix starting at i
# use binary search to get the next index for the DP transition.

# 1. Sort start, end, and profit according to the start time.
# 2.  If you choose to take job i skip all jobs that start before job i ends.  jump is used to find the index of the first job that starts after job i ends
# 3. Take a dynamic programming approach to determine the optimal profit.
# you can either take the job for profit[i] + helper(jump[i])
# or you can skip the job for helper(i + 1)

class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        n = len(start)
        start, end, profit = zip(*sorted(zip(start, end, profit)))
        jump = {i: bisect.bisect_left(start, end[i]) for i in range(n)}

        dp = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], profit[i] + dp[jump[i]])

        return dp[0]
