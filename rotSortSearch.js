// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
//
// (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
//
// You are given a target value to search. If found in the array return its index, otherwise return -1.
//
// You may assume no duplicate exists in the array.
//
// Your algorithm's runtime complexity must be in the order of O(log n).
//
// Example 1:
//
// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4
// Example 2:
//
// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        let first = nums[left];
        let last = nums[right];
        let midIdx = Math.floor((left + right) / 2) ;
        let mid = nums[midIdx];
        if (mid === target) return midIdx;
        if (first <= mid) {
            if (first <= target && target < mid) {
                right = midIdx - 1;
            } else {
                left = midIdx + 1;
            }
        } else {
            if (target <= last && mid < target) {
                left = midIdx + 1;
            } else {
                right = midIdx - 1;
            }
        }
    }
    return -1;
};
