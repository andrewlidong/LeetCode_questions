# The basic idea is that we set two pointers l and r to the left and right end of height. Then we get the minimum height (minHeight) of these pointers (similar to Container with Most Water due to the Leaking Bucket Effect) since the level of the water cannot be higher than it. Then we move the two pointers towards the center. If the coming level is less than minHeight, then it will hold some water. Fill the water until we meet some "barrier" (with height larger than minHeight) and update l and r to repeat this process in a new interval.

class Solution:
    def trap(self, height):
        n = len(height)
        l, r, water, minHeight = 0, n-1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water
