class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 1
        buy = 0
        profit = 0
        while sell<len(prices):
            if prices[sell]>= prices[buy]:
                profit += prices[sell] - prices[buy] 
                sell+=1
                buy+=1
              
            elif prices[buy]> prices[sell]:
                buy = sell
                sell+=1
            
        return profit if profit else 0


        