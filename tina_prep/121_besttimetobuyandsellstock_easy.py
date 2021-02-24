class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # store largestProfit which we will continually update
        largestProfit = float("-inf")
        # keep track of lowestPrice seen so far so we can continually calculate currentPrice accurately
        lowestPrice = float("inf")

        # iterate through prices
        for price in prices:
            # update lowestPrice
            lowestPrice = min(lowestPrice, price)
            # calculate currentProfit
            currentProfit = price - lowestPrice
            # potentially update largestProfit
            largestProfit = max(largestProfit, currentProfit)
        return largestProfit

# Time: O(N)
# Space: O(1)


# figure out the local minima and the local maxima on the other end.  Probably two pointers, one from the beginning, one from the end makes sense.
