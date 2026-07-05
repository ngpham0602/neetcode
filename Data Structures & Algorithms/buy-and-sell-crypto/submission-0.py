class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        largest = 0
        smallest = prices[0]
        for p in prices:
            smallest = min(smallest, p)
            largest = max(largest, p - smallest)

        return largest            
