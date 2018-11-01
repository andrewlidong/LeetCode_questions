def rob(nums)
    return 0 if nums.nil? || nums.length == 0

    maxAt = []
    maxAt.push({ robbed: nums.first, not_robbed: 0 })

    nums.each_with_index do |num, idx|
        next if idx == 0
        maxAt.push({
            robbed: maxAt[idx - 1][:not_robbed] + num,
            not_robbed: [maxAt[idx - 1][:robbed], maxAt[idx - 1][:not_robbed]].max
        })
    end

    n = nums.length
    return [maxAt[n-1][:robbed], maxAt[n - 1][:not_robbed]].max
end
