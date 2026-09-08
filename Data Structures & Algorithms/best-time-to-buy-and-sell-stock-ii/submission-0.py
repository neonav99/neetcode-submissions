class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        running_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                running_profit += profit
                l = l+1
            else:
                l = r
            r = r+1
        return running_profit


        