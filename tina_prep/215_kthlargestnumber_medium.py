import math


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]

# Time: O(NlogN)
# Space: O(N)


# Brute force with sorting
# use an in-place sort like a HeapSort to sort the input array to get the smallest number


#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # to handle duplicates, keep track of previous largest number and its index
#         previousLargestNum, previousLargestIndex = math.inf, -1
#         currentLargestNum, currentLargestIndex = -math.inf, -1

#         for i in range(k):
#             for j in range(len(nums)):
#                 if nums[j] < previousLargestNum and nums[j] > currentLargestNum:
#                     # found the next largest number
#                     currentLargestNum = nums[j]
#                     currentLargestIndex = j
#                 elif nums[j] == previousLargestNum and j > previousLargestIndex:
#                     # found a number which is equal to the previous largest number; since numbers can repeat
#                     # we will consider nums[j] only if it has a different index than the previous largest
#                     currentLargestNum = nums[j]
#                     currentLargestIndex = j
#                     break # break here as we have found our definitive next largest number

#             # current largest number becomes previous largest number for the next iteration
#             previousLargestNum = currentLargestNum
#             previousLargestIndex = currentLargestIndex
#             currentLargestNum = -math.inf

#         return previousLargestNum

# The simplest brute-force algorithm is to find the Kth largest number in a step by step fashion.  This means, first find the largest, then the 2nd largest, then the 3rd largest, and so on, until we have found the kth largest element.

# Time: O(N * K)
# Space: O(1)
