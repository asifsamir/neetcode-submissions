class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = 101
        max_profit = 0
        
        for price in prices:
            if price > smallest:
                max_profit = max(max_profit, (price - smallest))
            
            if price < smallest:
                smallest = price

        return max_profit