/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let maximum = 0;
    let l = 0;
    let r = height.length-1
    while (l <= r){
            currMax = (r - l)*Math.min(height[r], height[l]);
            maximum = Math.max(maximum, currMax);
            if (l <= r && height[l] < height[r]){
                l += 1
            }
            else if (l <= r && height[r] <= height[l]){
                r -= 1
            }
    }
        return maximum;
};