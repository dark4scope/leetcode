class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        mem = {}
        def dfs(piles, index, k):
            if index == len(piles):
                return 0
            if (index,k) in mem:
                return mem[(index, k)]

            cur = piles[index]
            res = 0
            cur_sum = 0
            for i in range(min(len(cur),k)):
                cur_sum += cur[i]
                res = max(res, cur_sum + dfs(piles, index+1, k-i-1))
            res = max(res, dfs(piles, index+1, k))
            mem[(index,k)] = res
            return res

        ans = dfs(piles, 0, k)
        # print(mem)
        return ans
    

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        f = [0] * (k + 1)
        sum_n = 0
        for pile in piles:
            n = len(pile)
            for i in range(1, n):
                pile[i] += pile[i - 1]  # pile 前缀和
            sum_n = min(sum_n + n, k)  # 优化：j 从前 i 个栈的大小之和开始枚举（不超过 k）
            for j in range(sum_n, 0, -1):
                f[j] = max(f[j], max(f[j - w - 1] + pile[w] for w in range(min(n, j))))  # w 从 0 开始，物品体积为 w+1
        return f[k]
