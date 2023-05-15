class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_value = prices[0]
        ans = 0
        for n in prices[1:]:
            if n < min_value:
                min_value = n
                max_value = n
            else:
                max_value = max(max_value, n)
                ans = max(ans,max_value-min_value)
        return ans