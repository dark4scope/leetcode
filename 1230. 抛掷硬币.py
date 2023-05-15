class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:

        n = len(prob)
        f = [[0.0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1.0
        for i in range(1, n + 1):
            for j in range(0, min(i + 1, target+1)):
                if j == 0:
                    f[i][j] = f[i - 1][j] * (1 - prob[i - 1])
                else:
                    f[i][j] = f[i - 1][j - 1] * prob[i - 1] + f[i - 1][j] * (1 - prob[i - 1])
        
        return f[n][target]
