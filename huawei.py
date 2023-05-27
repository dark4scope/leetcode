# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 示例 1：
# ￼
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 示例 2：

# 输入：height = [4,2,0,3,2,5]
# 输出：9

class Solution:
    def solve(self, height):
        height = [0] + height + [0]
        left = []
        right = []
        stack = []
        for n in height:
            while len(stack) != 0 and stack[-1] < n:
                stack.pop()
            if len(stack) == 0 or stack[-1] < n:
                stack.append(n)
            left.append(stack[-1])

        stack = []
        for n in height[::-1]:
            while len(stack) != 0 and stack[-1] < n:
                stack.pop()
            if len(stack) == 0 or stack[-1] < n:
                stack.append(n)
            right.append(stack[-1])
            
        right = right[::-1]
        print(left)
        print(right)
        ans = 0
        for x,y,n in zip(left, right,height):
            ans += min(x,y) - n
        return ans

s = Solution()
print(s.solve([0,1,0,2,1,0,1,3,2,1,2,1]))

