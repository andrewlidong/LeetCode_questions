class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            Solution.search_pair(nums, -nums[i], i + 1, triplets)
        return triplets

    def search_pair(nums, target_sum, left, return_array):
        right = len(nums) - 1
        while (left < right):
            current_sum = nums[left] + nums[right]
            if current_sum == target_sum:
                return_array.append([-target_sum, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif target_sum > current_sum:
                left += 1
            else:
                right -= 1


# Time: O(NlogN + N^2) which is asymptotically equal to O(N^2)
# Space: O(N)

# sort the array
# take each index, and then run twosum on the remainder of the array trying to find the complement
# skip over duplicates
