# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    current_profit = 0
    best_profit = 0
    first_day = { price: prices.first, day: 0 }
    second_day = { price: prices.first, day: 0 }
    prices.each_with_index do |price, day|
        if price > second_day[:price] || second_day[:day] < first_day[:day]
            second_day[:price] = price
            second_day[:day] = day
        end

        if price < first_day[:price]
            first_day[:price] = price
            first_day[:day] = day
        end

        if first_day[:day] < second_day[:day]
            current_profit = second_day[:price] - first_day[:price]
            best_profit = current_profit if best_profit.zero? || current_profit > best_profit
        end
    end
    best_profit
end
