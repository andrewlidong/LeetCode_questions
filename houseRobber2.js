const proRobber = function(nums) {
  const robPlan = function(nums, s, e) {
    let preMax = 0, curMax = 0;
    for (let i = s; i < e; i++) {
      let temp = curMax;
      curMax = Math.max(curMax, preMax + nums[i]);
      preMax = temp;
    }
    return curMax;
  };
  if (nums.length == 1) return nums[0];
  if (nums.length < 1 || nums == null) return 0;

  let start0 = robPlan(nums, 0, nums.length - 1);
  let start1 = robPlan(nums, 1, nums.length);
  return Math.max(start0, start1);
};
