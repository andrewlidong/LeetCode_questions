# class Solution:
#     def maxSlidingWindow(self, nums, k):
#         n = len(nums)
#         if n * k == 0:
#             return []
#         if k == 1:
#             return None

#         left = [0] * n
#         left[0] = nums[0]
#         right = [0] * n
#         right[n - 1] = nums[n - 1]
#         for i in range(1, n):
#             # from left to right
#             if i % k == 0:
#                 # block start
#                 left[i] = nums[i]
#             else:
#                 left[i] = max(left[i - 1], nums[i])
#             # from right to left
#             j = n - i - 1
#             if (j + 1) % k == 0:
#                 # block end
#                 right[j] = nums[j]
#             else:
#                 right[j] = max(right[j + 1], nums[j])

#         output = []
#         for i in range(n - k + 1):
#             output.append(max(left[i + k - 1], right[i]))

#         return output

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current elements nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

# Time: O(N) since each element has its index added and then removed from the queue
# Space Complexity: O(N) since O(N - j + 1) is used for an output array and O(k) for a deque

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         windowMax = float("-inf")
#         maxSlidingWindow = [None] * (len(nums) - k + 1)
#         currentWindow = []
#         windowStart = 0
#         for window_end in range(len(nums)):


# Input: an array of integers nums and an integer sliding window of size k moving from the very left of the array to the very right.  -> Output: the max sliding window

# consider using a deque (double-ended queue)
# the queue size doesn't necessarily need to be the same size as the window size
# Remove redundant elements and the queue should store only elements that need to be considered.

# Process the first k elements separately to initiate the deque
# Iterate over the array.  At each step:
# Clean the deque:
# Keep only the indexes of elements from the current sliding window
# Remove indexes of all elements smaller than the current one, since they will not be the maximum ones
# Append the current element to the deque
# Append deque[0] to the output
# Return the output array

# hammer method

# class Solution:
#     def maxSlidingWindow(nums, k):
#         n = len(nums)
#         if n * k == 0:
#             return []

#         return [max(nums[i:i + k]) for i in range(n - k + 1)]

# # Time complexity: O(Nk) where N is a number of elements in the array
# # Space complexity: O(N - k + 1) for an output array
