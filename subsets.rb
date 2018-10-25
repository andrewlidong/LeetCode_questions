# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#

# @param {Integer[]} nums
# @return {Integer[][]}
def subsets(nums)
    (0..nums.size).flat_map { |k| nums.combination(k).to_a }
end

# @param {Integer[]} nums
# @return {Integer[][]}
def subsets(nums)
    subsets = [[]]
    nums.each { |n| subsets += subsets.map { |s| s + [n] } }
    subsets
end

# @param {Integer[]} nums
# @return {Integer[][]}
def subsets(nums)
    nums.reduce([[]]) { |subsets, n| subsets + subsets.map { |s| s + [n] }}
end
