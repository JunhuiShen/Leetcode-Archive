# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note:

# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.
 

# Example 1:

# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Example 2:

# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
 

# Constraints:

# 1 <= prices.length <= 5 * 104
# 1 <= prices[i] < 5 * 104
# 0 <= fee < 5 * 104

from collections import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        if n == 0:
            return 0
        
        buy_list = [0] * (len(prices))
        sell_list = [0] * (len(prices))

        buy_list[0] = -prices[0] # Buying on the first day

        for i in range(1, n):
            # The max profit if we buy on day i is either:
            # 1. We continue with the decision to buy from the previous days, or
            # 2. We sell the stock we held and buy new stock on day i (taking fee into account)
            buy_list[i] = max(buy_list[i-1], sell_list[i-1] - prices[i])

            # The max profit if we sell on day i is either:
            # 1. We continue with the decision to sell from the previous days, or
            # 2. We sell the stock we bought earlier on day i
            sell_list[i] = max(sell_list[i-1], buy_list[i] + (prices[i] - fee) )
        # The result is the maximum profit we can have after the last day, with no stock in hand

        return sell_list[-1]