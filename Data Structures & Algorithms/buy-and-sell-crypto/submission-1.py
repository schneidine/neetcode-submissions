class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution - O(n) Time, O(1) Space
        # no list
        if not prices:
            return 0

        # init profit to 0
        profit = 0
        # sell is our last possible date to sell - last index
        sell = len(prices) - 1
        # buy is at first possible day available from sell, index before last
        buy = sell - 1

        # while there are still days to buy
        while buy >=0:
            # if our current buy/sell is more profitable
            if prices[sell] - prices[buy] >= profit:
                # save that combos profit 
                profit = prices[sell] - prices[buy]
            # else if not, check if this is a better day to sell
            #  than our current pick and update
            elif prices[sell] < prices[buy]:
                sell = buy
            
            # move onto next buy date
            buy = buy-1
        
        # return answer
        return(profit)