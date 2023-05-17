class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[] # 构建一个栈记录字符index
        ans=0
        for i in range(len(s)):
            # 如果栈非空，且当前为右括号，且有记录的左括号，则出栈
            if stack and s[i]==")" and s[stack[-1]]=="(":
                stack.pop()
                # 如果出栈后变成空栈，则说明整个[0:i]的区间都是合格的，长度为i+1
                # 如果出栈后非空，则说明区间[stack[-1]:i]是合格的
                ans=max(ans,i-(stack[-1] if stack else -1))
            else:
                # 以下3个条件会触发else
                # 如果是空栈
                # 或者当前字符为左括号（需要寻找匹配的右括号）
                # 或者当前字符为右括号，而且栈顶记录的也是右括号（不合格的情况，永远不会被pop）
                stack.append(i)
                
        return ans
    

# 动态规划也很巧妙啊
    class Solution:
        def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == '(':
                continue
            # s[i] is ')'
            if s[i - 1] == '(':
                dp[i] = 2
                if i >= 2:
                    dp[i] += dp[i - 2]
            elif dp[i - 1] > 0:
                # s[i - 1] is ')' and is a valid end
                y = i - 1 - dp[i - 1]
                if y >= 0 and s[y] == '(':
                    dp[i] = dp[i - 1] + 2
                    if y >= 1:
                        dp[i] += dp[y - 1]
            res = max(res, dp[i])
        
        return res