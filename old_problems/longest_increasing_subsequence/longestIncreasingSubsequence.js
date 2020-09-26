/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    var seqLengths = [Number.POSITIVE_INFINITY];
    const len = nums.length;
    for (var i = len - 1; i >= 0; i--) {
        var num = nums[i];
        for (var length = seqLengths.length; length > 0; length--) {
            if (num < seqLengths[length - 1]) {
                if (!seqLengths[length]) { seqLengths[length] = Number.NEGATIVE_INFINITY; }
                seqLengths[length] = Math.max(seqLengths[length], num);
                break;
            }
        }
    }
    return seqLengths.length - 1;
};
