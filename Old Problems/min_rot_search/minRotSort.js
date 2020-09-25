// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
//
// (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
//
// Find the minimum element.
//
// You may assume no duplicate exists in the array.
//
// Example 1:
//
// Input: [3,4,5,1,2]
// Output: 1
// Example 2:
//
// Input: [4,5,6,7,0,1,2]
// Output: 0

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    if (nums[0] < nums[nums.length - 1]) return nums[0];
    if (nums.length === 0) return null;
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        let midIdx = Math.floor((left + right) / 2);
        let mid = nums[midIdx];
        let afterMid = nums[midIdx + 1];
        let first = nums[left];
        if (afterMid < mid) {
            return afterMid;
        } else if (first < mid) {
            left = midIdx + 1;
        } else {
            right = midIdx;
        }
    }
    return nums[left];
};
