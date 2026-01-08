class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 1
        buy = 0
        profit = 0
        while sell<len(prices):
            if prices[sell]> prices[buy]:
                profit += prices[sell]- prices[buy]
                sell+=1
                buy+=1
            else:
                buy+=1
                sell+=1
        return profit

        