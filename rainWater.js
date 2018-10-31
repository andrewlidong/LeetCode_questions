const getMin = (a, b) => a < b ? a : b;

/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    const maxLeft = [];
    let currentMaxLeft = 0;
    for (let i = 0; i < height.length; i += 1) {
      maxLeft.push(currentMaxLeft);
      if (height[i] > currentMaxLeft) {
        currentMaxLeft = height[i];
      }
    }
    const maxRight = [];
    let currentMaxRight = 0;
    for (let i = height.length - 1; i >= 0; i -= 1){
      maxRight[i] = currentMaxRight;
      if (height[i] > currentMaxRight) {
        currentMaxRight = height[i];
      }
    }

    //now loop through each one and check the max left and max right at that index
    let rainTrapped = 0;
    for (let i = 0; i < height.length; i += 1) {
      if (maxLeft[i] !== 0 && maxRight[i] !== 0) {
        maxWater = getMin(maxLeft[i], maxRight[i]);
        if (maxWater > height[i]) {
          rainTrapped += maxWater - height[i];
        }
      }
    }
    return rainTrapped;
};
