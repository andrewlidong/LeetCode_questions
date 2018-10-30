# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    return [] if nums.size < 2

    lookup = {}

    for index in (0..nums.size - 1)
        return [index, lookup[target - nums[index]]] if lookup[target - nums[index]]

        lookup[nums[index]] = index
    end

    return []
end
