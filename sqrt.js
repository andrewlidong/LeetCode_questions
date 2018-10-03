// Implement int sqrt(int x).
//
// Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
//
// Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
//
// Example 1:
//
// Input: 4
// Output: 2
// Example 2:
//
// Input: 8
// Output: 2
// Explanation: The square root of 8 is 2.82842..., and since
//              the decimal part is truncated, 2 is returned.

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (x < 2) return x;
    let left = 0;
    let right = Math.floor(x / 2);
    while (left <= right) {
      let mid = Math.floor((left + right) / 2);
      let post = mid + 1;
      if (mid * mid <= x && post * post > x) {
        return mid;
      } else if (mid * mid > x) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
};
