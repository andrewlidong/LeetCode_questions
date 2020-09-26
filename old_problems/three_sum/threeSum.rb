# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# @param {Integer[]} nums
# @return {Integer[][]}
def three_sum(nums)
    nums.sort!
    seen = Hash.new
    results = []
    nums.each_with_index do |e, i|
        if !seen.has_key?(e)
            two_sum(nums[i+1 .. -1], 0 - e).each do |pair|
                results << [e] + pair.map{ |j| nums[j + i + 1] }
            end
            seen[e] = i
        end
    end
    return results.uniq
end

def two_sum(nums, target)
    seen = Hash.new
    result = []
    nums.each_with_index do |e, i|
        if seen.has_key?(target - e)
            result << [seen[target - e], i]
        else
            seen[e] = i
        end
    end
    return result
end
