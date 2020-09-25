// https://leetcode.com/problems/reverse-integer/description/
//
// Reverse Integer
//
// Given a 32-bit signed integer, reverse digits of an integer.
//
// Example 1:
//
// Input: 123
// Output: 321
// Example 2:
//
// Input: -123
// Output: -321
// Example 3:
//
// Input: 120
// Output: 21
// Note:
// Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
//


/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let max = Math.pow(2, 31) -1;
    let min = Math.pow(-2, 31);
    let remainder = 0;
    let res = 0;
    while(x) {
        remainder = x % 10;
        res = res * 10 + remainder;
        x = parseInt(x / 10);
        if (res < min || res > max) return 0;
    }

    return res;
};
