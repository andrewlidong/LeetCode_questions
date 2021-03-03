# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         output = []
#         for i in reversed(range(len(nums))):
#             if nums[i] > nums[i - 1]:
#                 nums[i], nums[i - 1] = nums[i - 1], nums[i]
#                 return nums
#             else:
#                 output.append(nums[i])
#         return output

# input: list of integers -> output: list of integers permuted to be a little greater, or sorted in ascending order.

# this boils down to figuring out if an array is monotonically decreasing, and trying to get it to monotonically decrease.
# We can probably check from the back for monotonically increasing actually.
# all the while we can append values?

# Solution:
# Find the next lexicographic permutation of the given list of numbers

# Approach 1: Brute Force
# Find every possible permutation of list formed by the elements of the given array and find out the permutation which is just larger than the given one.  This will be a very naive approach, since it requires us to find out every possible permutation which will take really long time.  This approach isn't really acceptable because of the complexity of the implementation and the time complexity.
# Time: O(N!) since the total number of possible permutations is n!
# Space: O(N) sicne an array will be used to store all the permutations.

# Approach 2: Single Pass Approach
# Observe that, for any given sequence in descending order, no next larger permutation is possible.
# Find the first pair of two successive numbers a[i] and a[i - 1] which satisfy a[i] > a[i - 1].  No rearrangement to the right of a[i - 1] can create a larger permutation since that subarray consists of numbers in descending order.
# what kind of rearrangement will produce the next larger number?  Replace the number a[i - 1] with the number just larger than itself among the numbers lying to its right section.
# Swap numbers a[i - 1] and a[j].
# Time complexity: O(n) in the worst case, only two scans of the whole array are needed
# Space complexity: O(1) since no extra space is used, in place replacements are done.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:  # nums are in descending order
            nums.reverse()
            return
        k = i - 1  # find the last 'ascending' position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k + 1, len(nums) - 1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
