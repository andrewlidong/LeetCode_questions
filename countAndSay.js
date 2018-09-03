// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/
//
// Count and Say
//
// The count-and-say sequence is the sequence of integers with the first five terms as following:
//
// 1.     1
// 2.     11
// 3.     21
// 4.     1211
// 5.     111221
// 1 is read off as "one 1" or 11.
// 11 is read off as "two 1s" or 21.
// 21 is read off as "one 2, then one 1" or 1211.
// Given an integer n, generate the nth term of the count-and-say sequence.
//
// Note: Each term of the sequence of integers will be represented as a string.
//
// Example 1:
//
// Input: 1
// Output: "1"
// Example 2:
//
// Input: 4
// Output: "1211"

/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    if (n === 1) {
        return "1";
    } else {
        let prevSeq = countAndSay(n - 1);
        let output = "";
        let count = 1;

        for (let i = 0; i < prevSeq.length; i++) {
            if (prevSeq[i + 1] === prevSeq[i]) {
                count += 1;
            } else {
                output += count.toString() + prevSeq[i];
                count = 1;
            }
        }

        return output;
    }
};
