class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # base case
        if 1 not in nums:
            return 1

        # nums = [1]
        if n == 1:
            return 2

        # replace negative numbers, zeros and numbers larger than n by 1s.  After this nums will contain only positive numbers
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # use index as a hash key and number sign as as presence detector.  If nums[1] is negative, that means that number [1] is present in the array.  If nums[2] is positive - number 2 is missing
        for i in range(n):
            a = abs(nums[i])
            # if you meet number a in the array - change the sign of the a-th element.
            # be careful with duplicates: do it only once
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])

        # now the index of the first positive number is equal to the first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n

        return n + 1

# input: array of integer nums, unsorted -> output: find the smallest positive missing integer
# Think about how to solve this problem in non-constant space
# Don't care about duplicates or non-positive integers
# O(2n) = O(n

# first get rid of negative numbers and zeroes since there's no need for them.  We can also get rid of all numbers larger than n as well, since the first missing positive is less than or equal to n + 1.
# now that we have an array with only positive numbers in a range from 1 to n, the problem is to find a first missing positive in O(N) time and constant space.
# if we could have a hash-map positivenumber -> its presence
# dirty workaround would be to allocate a string hash_str with n zeros, and use it as a sort of hash map by changing hash_str[i] to 1 each time one meets number i in the array.
# use index in nums as a hash key and sign of the element as a hash value which is a presence detector.
# Walk along the cleaned array, check each element value and change the sign of element to negative to mark that number is present in nums.  Be careful with duplicates and ensure that the sign was changed only once.

# Check if 1 is present in the array.  If not, 1 is the answer.
# if nums = [1] the answer is 2
# replace negative numbers, zeroes, and numbers larger than n by 1s.
# walk along the array.  Change the sign of a element if you meet number a.  Be careful with duplicates: do sign changes only once.  Use index 0 to save information about the presence of a number n since index n is not available.
# Walk again along the array.  Return the index of the first positive element.
# if nums[0] > 0 return n
# If, on the previous step you didn't find the positive element in nums, that means the answer is n + 1

# cycle sort solution

# def firstMissingPositive(self, nums: List[int]) -> int:
#     i = 0
#     n = len(nums)
#     while i < n:
#         j = nums[i] - 1
#         # put nums[i] to the correct place if nums[i] in the range [1, n]
#         if 0 <= j < n and nums[i] != nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]
#         else:
#             i += 1

#         # so far, all the integers that could find their own correct place have been put to the correct place, we need to find out which is occupied wrongly.
#     for i in range(n):
#         if nums[i] != i + 1:
#             return i + 1
#     return n + 1
