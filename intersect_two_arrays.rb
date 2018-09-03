# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
#
# Intersection of Two Arrays II
#
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersect(nums1, nums2)
    nums = Hash.new(0)
    return_arr = []

    nums1.each do |num|
        nums[num] += 1
    end

    nums2.each do |num|
        return_arr << num if nums[num] > 0
        nums[num] -= 1
    end

    return_arr
end
