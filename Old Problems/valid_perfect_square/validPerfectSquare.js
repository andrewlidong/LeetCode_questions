// Given a positive integer num, write a function which returns True if num is a perfect square else False.
//
// Note: Do not use any built-in library function such as sqrt.
//
// Example 1:
//
// Input: 16
// Output: true
// Example 2:
//
// Input: 14
// Output: false

var isPerfectSquare = function(num) {
  let left = 0;
  let right = Math.ceil(num / 2);

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    let square = mid * mid;
    if (square === num) {
      return true;
    } else if (square < num) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return false;
};
