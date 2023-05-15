# 正则表达式匹配
class Solution(object):
    def isMatch(self, s, p):
        s = '1' + s # 处理前置字符
        p = '1' + p # 处理前置字符
        m = len(s)
        n = len(p)
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(1, n+1): # pattern
            for j in range(1, m+1): # str
                if p[i-1] == '.' or p[i-1] == s[j-1]: # 本字符匹配成功
                    dp[i][j] |= dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] |= dp[i-2][j] # 出现0个前置字符
                    dp[i][j] |= dp[i-1][j] # 出现1个前置字符
                    last_char = p[i-2] # *号重复匹配的字符
                    if dp[i][j]: # 如果当前状态是匹配的，那么递推s串后续匹配状态
                        for j in range(j,m+1):
                            if s[j-1] == last_char or p[i-2] == '.':
                                dp[i][j] |= True
                            else: # 如果某个位置开始不匹配，那么退出循环
                                break
        return dp[-1][-1]
    