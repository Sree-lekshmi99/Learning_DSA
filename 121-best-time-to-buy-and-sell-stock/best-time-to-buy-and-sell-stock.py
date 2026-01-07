class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = prices[0]
        buy = 0
        sell =1
        while sell<len(prices):
            # if prices[buy] ==0:
            #     buy+=1
            # if prices[sell] ==0:
            #     sell+=1

            if prices[buy] > prices[sell]:
                buy=sell
                
            elif prices[buy]<=prices[sell]:
                profit = prices[sell]- prices[buy]
                max_profit = max(max_profit, profit)
            sell+=1
            # elif prices[buy] ==0 or prices[sell] ==0

        return max_profit

        