# @param {Integer[]} nums
# @return {Integer[][]}
def permute(nums)
    perms = []

    perms << [] if nums.empty?

    nums.each_with_index do |num, idx|
        prev_perms = permute(nums[0...idx] + nums[idx+1..-1])
        prev_perms.each do |perm|
            perms << [num] + perm
        end
    end

    perms
end
