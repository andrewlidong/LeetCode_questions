// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
//
// Move Zeroes
//
// Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
//
// Example:
//
// Input: [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Note:
//
// You must do this in-place without making a copy of the array.
// Minimize the total number of operations.

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    for (let i = nums.length - 1; i >= 0; i--) {
        if (nums[i] === 0) {
            let zero = nums.splice(i,1) [0];
            nums.push(zero);
        }
    }
};

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let timesExecuted = 0;
    let i = 0;
    while (i < nums.length && timesExecuted < nums.length) {
        nums[i] === 0 ? nums.push(nums.splice(i,1)[0]) : i++;
        timesExecuted++;
    }
};
