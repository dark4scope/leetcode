# 原始想法是判断背包的存在性问题，然后求最大连续子序列的长度。但是问题的规模不允许这种算法。背包的target太大了。
# 题解中使用贪心算法，学习一下
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        ans = 1
        for v in sorted(coins):
            if v > ans:
                break
            ans += v
        return ans