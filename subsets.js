// Given a set of distinct integers, nums, return all possible subsets (the power set).
//
// Note: The solution set must not contain duplicate subsets.
//
// Example:
//
// Input: nums = [1,2,3]
// Output:
// [
//   [3],
//   [1],
//   [2],
//   [1,2,3],
//   [1,3],
//   [2,3],
//   [1,2],
//   []
// ]

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    if (nums.length === 0 || nums === null) return [];
    let returnArr =[];
    returnArr.push([]);
    nums.forEach(num => {
        let len = returnArr.length;
        let i = 0;
        while (i < len) {
            let temp = returnArr[i].slice(0);
            temp.push(num);
            returnArr.push(temp);
            i++;
        }
    });

    return returnArr;
};
