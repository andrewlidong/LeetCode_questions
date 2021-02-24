class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0]*length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer

# Time Complexity: O(N) where N represents the number of elements in the input array.  We use one iteration to construct the array L, one to update the array answer
# Space Complexity: O(1) since we don't use any additional array for our computations.


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # the length of the input array
#         length = len(nums)

#         # the left and right arrays as described in the algorithm
#         left = [0] * length
#         right = [0] * length
#         results = [0] * length

#         # left[i] contains the products of all elements to the left
#         # for the element at index 0, there are no elements to the left, so left[0] = 1
#         left[0] = 1
#         for i in range(1, length):
#             # left[i - 1] already contains the product of elements to the left of i - 1
#             # simply multiplying it with nums[i - 1] would give the product of all elements to the left of index 'i'
#             left[i] = nums[i - 1] * left[i - 1]

#         # right[i] contains the product of all the elements to the right
#         # for the element at index 'length - 1' there are no elements to the right, so right[length - 1] = 1
#         right[length - 1] = 1
#         for i in reversed(range(length - 1)):
#             # right[i + 1] already contains the product of elements to the right of 'i + 1'
#             # simply multiplying it with nums[i + 1] would give the product of all elements to the right of index i
#             right[i] = nums[i + 1] * right[i + 1]

#         # constructing the results array
#         for i in range(length):
#             # for the first element, right[i] would be product except self
#             # for the last eleemnt, the product except itself would be left[i]
#             # otherwise, multiply product of all elements to the left and to the right
#             results[i] = left[i] * right[i]

#         return results

# # Time Complexity: O(N) where N is the number of elements in the input array.  One iteration to construct left, one to construct right, and the last to construct the answer array using left and right.
# # Space Complexity: O(N) used up by the two intermediate arrays that we constructed to keep track of product of elements to the left and right.


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         leftProducts = []
#         runningLeft = 1
#         rightProducts = []
#         runningRight = 1
#         results = []

#         for i in nums:
#             runningLeft *= i
#             leftProducts.append(runningLeft)
#         for j in reversed(nums):
#             runningRight *= j
#             rightProducts.append(runningRight)

#         for k in range(len(nums)):
#             if k == 0:
#                 results.append(rightProducts[1])
#             if k == len(nums) - 1:
#                 results.append(leftProducts[-2])
#             else:
#                 results.append(leftProducts[k - 1] * rightProducts[k + 1])

#         return results

# The easy way to solve it is to multiply everything together, and then iterate through and divide each number by itself.
# I think there's a left right pointer solution too, where we multiply up each pointer
# create a left running multiplier and a right running multiplier, and basically at each point multiply left - 1 by right + 1
