// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
//
// First Unique Character in a String
//
// Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
//
// Examples:
//
// s = "leetcode"
// return 0.
//
// s = "loveleetcode",
// return 2.
// Note: You may assume the string contain only lowercase letters.

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    let hsh = {};

    for (let i = 0; i < s.length; i++) {
        hsh[s[i]] ? (hsh[s[i]] = hsh[s[i]].concat(i)) : (hsh[s[i]] = [i]);
    }

    for (let ch in hsh) {
        if (hsh[ch].length === 1) {
            return hsh[ch][0];
        }
    }

    return -1;
};
