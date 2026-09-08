class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        for index_buy,buy in enumerate(prices):
            for sell in prices[index_buy:]:
                temp_val = sell - buy
                if max_value <= temp_val:
                    max_value = temp_val
        return max_value


        
        