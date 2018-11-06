def sort_colors(nums)
  zero = zero_or_one = -1
  for i in 0...nums.size
    curr = nums[i]; nums[i] = 2
    nums[zero_or_one += 1]  = 1 if curr <= 1
    nums[zero += 1]         = 0 if curr == 0
  end
end
