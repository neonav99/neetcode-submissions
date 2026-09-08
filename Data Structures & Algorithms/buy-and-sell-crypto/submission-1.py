class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        l_price = prices[0]
        for buy in prices:
            if l_price < buy:
                temp_val = buy-l_price
                if temp_val>max_value:
                    max_value = temp_val
            else:
                l_price = buy
        return max_value
            


        
        