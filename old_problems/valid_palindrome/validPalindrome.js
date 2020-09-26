// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
//
// Valid Palindrome
//
// Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
//
// Note: For the purpose of this problem, we define empty string as valid palindrome.
//
// Example 1:
//
// Input: "A man, a plan, a canal: Panama"
// Output: true
// Example 2:
//
// Input: "race a car"
// Output: false

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    charStr = s.toLowerCase().replace(/\W/g, "");
    const midPoint = Math.floor(charStr.length / 2);

    for (let i = 0; i < midPoint; i++) {
        endPoint = charStr.length - i - 1;
        if (charStr[i] !== charStr[endPoint]) {
            return false;
        }
    }

    return true;
};
