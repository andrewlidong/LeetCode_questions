# Time: O(N)
# Space: O(N)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        # Make a Set with the input
        nums = set(nums)

        # Find the maximum
        maximum = max(nums)

        # Check whether or not this is a case where we need to return the maximum
        if len(nums) < 3:
            return maximum

        # Otherwise, continue on to finding the third maximum.
        nums.remove(maximum)
        second_maximum = max(nums)
        nums.remove(second_maximum)
        return max(nums)

    # Time: O(N)
    # Space: O(1)
    def thirdMax(self, nums: List[int]) -> int:

        def maximum_ignoring_seen_maximums(nums, seen_maximums):
            maximum = None
            for num in nums:
                if num in seen_maximums:
                    continue
                if maximum == None or num > maximum:
                    maximum = num
            return maximum

        seen_maximums = set()

        for _ in range(3):
            current_maximum = maximum_ignoring_seen_maximums(
                nums, seen_maximums)
            if current_maximum == None:
                return max(seen_maximums)
            seen_maximums.add(current_maximum)

        return min(seen_maximums)


def thirdMax(self, nums: List[int]) -> int:
    maximums = set()
    for num in nums:
        maximums.add(num)
        if len(maximums) > 3:
            maximums.remove(min(maximums))
    if len(maximums) == 3:
        return min(maximums)
    return max(maximums)
