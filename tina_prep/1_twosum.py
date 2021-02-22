class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for (idx, num) in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], idx]
            else:
                seen[num] = idx
        return []

# Time: O(N) where N is the size of nums
# Space: O(N) where N is the size of nums

# create a results array
# create a set of numbers to push numbers into along with their indices
# iterate through the given nums list, checking if the target - num is in the set.
# push num into set
# continue searching until target - num is in the set.  If so, return the indices.  We can do this eagerly or we can populate the results with the indices


# must do this instead of sorting array, since we lose indices when we sort.

# alternatively we can create a nested for loop, but this trades our time complexity to O(N^2)
