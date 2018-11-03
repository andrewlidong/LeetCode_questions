class Solution:
    def lengthOfLIS(self, nums):
        dp = []
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)
