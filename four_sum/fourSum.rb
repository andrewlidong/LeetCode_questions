# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[][]}
def four_sum(nums, target)
    return [] if nums.empty? || nums.max * 4 < target
    solutions = {}
    nums.combination(4).each do |subset|
        next if subset.sum != target || solutions[subset]
        sorted = subset.sort
        solutions[sorted] = true unless solutions[sorted]
    end

    solutions.keys
end
