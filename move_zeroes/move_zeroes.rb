# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
    i = 0
    timesExecuted = 0
    while i < nums.length && timesExecuted < nums.length
        nums[i].zero? ? nums.push(nums.delete_at(i)) : i+=1
        timesExecuted += 1
    end
end
