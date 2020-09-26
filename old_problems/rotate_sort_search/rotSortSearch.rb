# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}

def search(nums, target)
    left = 0
    right = nums.length - 1
    while left <= right
      first = nums[left]
      midIdx = (left + right)/2
        mid = nums[midIdx]
        last = nums[right]
        return midIdx if mid == target
        if mid < last # right half is sorted
            if mid < target && target <= last
                left = midIdx + 1
            else
                right = midIdx - 1
            end
        else # left half is sorted
            if first <= target && target < mid
                right = midIdx - 1
            else
                left = midIdx + 1
            end
        end
    end
    -1
end
