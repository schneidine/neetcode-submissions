class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # no list
        if not prices:
            return 0

        profit = 0
        sell = len(prices) - 1
        buy = sell - 1

        while buy >=0:
            if prices[sell] - prices[buy] >= profit:
                profit = prices[sell] - prices[buy]
            elif prices[sell] < prices[buy]:
                sell = buy

            buy = buy-1

        return(profit)