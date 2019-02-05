# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
#
#
# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
# Example 2:
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
# Note:
#
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].

# Iterative solution
def iter_search(nums, target)
  return -1 if nums.nil? || nums.empty?
  left = 0
  right = nums.length - 1
  while left <= right
    mid = (left + right) / 2
    if nums[mid] == target
      return mid
    elsif nums[mid] < target
      left = mid + 1
    else
      right = mid - 1
    end
  end
  -1
end

# Recursive Solution
def rec_search(nums, target)
  return -1 if nums.empty?
  midIdx = nums.length / 2
  mid = nums[midIdx]
  if mid == target
    return midIdx
  elsif mid < target
    idx = rec_search(nums[midIdx+1..-1], target)
    return -1 if idx == -1
    return idx + midIdx + 1
  elsif mid > target
    return rec_search(nums[0...midIdx], target)
  end
end
