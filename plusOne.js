// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
//
// Plus One
//
// Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
//
// The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
//
// You may assume the integer does not contain any leading zero, except the number 0 itself.
//
// Example 1:
//
// Input: [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Example 2:
//
// Input: [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    if (digits[digits.length - 1] < 9) {
        digits[digits.length - 1] += 1;
    } else {
        let i = digits.length - 1;
        let carryOver = true;

        while (digits[i] + 1 > 9 && carryOver === true) {
            carryOver = false;
            digits[i] = 0;

            if (digits[i - 1]) {
                digits[i - 1] += 1;
                if (digits[i - 1] > 9) {
                    carryOver = true;
                }
            } else {
                digits.unshift(1);
            }
            i--;
        }
    }

    return digits;
};
