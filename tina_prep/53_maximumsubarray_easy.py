class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = float('-inf')

        for num in nums:
            currentSum += num
            maxSum = max(maxSum, currentSum)
            # reset if we're ever negative
            if currentSum < 0:
                currentSum = 0

        return maxSum

# Time: O(N)
# Space: O(1)

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         largestSum = float('-inf')
#         windowStart = 0
#         windowSum = 0
#         for windowEnd in range(len(nums)):
#             windowSum += nums[windowEnd]
#             if windowSum > largestSum:
#                 largestSum = windowSum
#                 continue
#             else:
#                 windowSum -= nums[windowStart]
#                 windowStart += 1
#         return largestSum

# # Input: integer array of nums
# # Output: Contiguous largest sum contiguous subarray sum

# # Use a sliding window, storing the largest sum, outputting it once we reach the end
