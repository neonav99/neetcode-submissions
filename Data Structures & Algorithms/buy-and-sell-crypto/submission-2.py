class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                pr = prices[r] - prices[l]
                max_profit = max(pr,max_profit)
            else:
                l = r
            r+=1
        return max_profit
        