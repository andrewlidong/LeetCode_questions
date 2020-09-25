# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
# Input: [3,4,5,1,2]
# Output: 1
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0

# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
    return nums.first if nums.first < nums.last
    left = 0
    right = nums.length - 1
    while left < right
        midIdx = (left + right) / 2
        mid = nums[midIdx]
        afterMid = nums[midIdx + 1]
        if mid > afterMid
            return afterMid
        elsif mid < nums[left]
            right = midIdx
        else
            left = midIdx + 1
        end
    end
    return nums[left]
end
