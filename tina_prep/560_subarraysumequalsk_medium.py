class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1

        return count


# whenever the sum has increased by a value of k, we've found a subarray of sums = k

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     count = 0
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             if sum(nums[i:j + 1]) == k:
    #                 count += 1
    #     return count

    # Brute force O(N^3) time solution, won't be accepted by leetcode

#     def subarraySum(self, nums: List[int], k: int) -> int:
#         if len(nums) == 1:
#             if nums[0] == k:
#                 return 1
#             else:
#                 return 0

#             # O(N^2) solution
#             count = 0
#             i, j = 0, 1
#             while j < len(nums):
#                 sub = nums[i: j + 1]
#                 if sum(sub) == k: # increment count and push window forward
#                     count += 1
#                     j += 1
#                 elif sum(sub) < k: # expand window
#                     j += 1
#                 else: #shrink
#                     i += 1

#             return count

#         # weird window sliding solution, doesn't work

#     def subarraySum(self, nums: List[int], k: int) -> int:
#             if len(nums) == 1:
#                 if nums[0] == k:
#                     return 1
#                 else:
#                     return 0

#                 # O(N) solution
#                 count = 0
#                 i, j = 0, 1
#                 s = nums[i: j + 1]
#                 while j < len(nums):
#                     if s == k: # increment count and then push window forward
#                         count += 1
#                         j += 1
#                     elif s < target: # expand window - if sum goes beyond target it will go to the else and window will shrink
#                         j += 1
#                         s += nums[j]
#                     else:
#                         # shrink
#                         s -= nums[i]
#                         i += 1

#                 return count

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         windowStart = 0
#         runningSum = 0
#         contiguousSubarrays = 0

#         for windowEnd in range(len(nums)):
#             runningSum += nums[windowEnd]
#             if runningSum == k:
#                 contiguousSubarrays += 1

#             while runningSum >= k:
#                 runningSum -= nums[windowStart]
#                 windowStart += 1

#         if runningSum == k:
#             contiguousSubarrays += 1

#         return contiguousSubarrays


# input: array of integers nums, integer k -> output: number of contiguous subarrays whose sum equals k

# Solution:
# Sliding window approach
# store windowstart, runningsum, and number of contiguous subarrays
# iterate through windowEnd indices
# slide window anytime we're greater than or not quite equal to k
# notice we don't need to sort, they've got to be contiguous anyways.
# increment contiguous subarray count everytime we get a runningsum equal to k.
# return contiguous subarray count at the end of our iteration
