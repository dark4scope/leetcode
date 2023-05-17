class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        @lru_cache(None)
        def dfs(x, y1, y2):
            res = grid[x][y1] + grid[x][y2]
            if y1 == y2:
                res //= 2
            if x == m - 1:
                return res

            nex = 0
            for b1 in [y1 - 1, y1, y1 + 1]:
                if 0 <= b1 < n:
                    for b2 in [y2 - 1, y2, y2 + 1]:
                        if 0 <= b2 < n:
                            nex = nex if nex > dfs(x + 1, b1, b2) else dfs(x + 1, b1, b2)
            return res + nex

        m, n = len(grid), len(grid[0])
        return dfs(0, 0, n - 1)
    

    class Solution:
        def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        pre = [[0] * n for _ in range(n)]
        for j1 in range(n):
            for j2 in range(j1, n):
                pre[j1][j2] = grid[m-1][j1] + grid[m-1][j2]
                if j1 == j2:
                    pre[j1][j2] -= grid[m-1][j1]

        for i in range(m-2, -1, -1):
            cur = [[0] * n for _ in range(n)]
            for j1 in range(n):
                for j2 in range(j1, n):
                    val = 0
                    for y1 in [j1 - 1, j1, j1 + 1]:
                        if 0 <= y1 < n:
                            for y2 in [j2 - 1, j2, j2 + 1]:
                                if 0 <= y2 < n:
                                    val = val if val > pre[y1][y2] else pre[y1][y2]
                    cur[j1][j2] = val + grid[i][j1] + grid[i][j2]
                    if j1 == j2:
                        cur[j1][j2] -= grid[i][j1]
            pre = cur[:]

        return pre[0][n-1]