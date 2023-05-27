from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        c_dict = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        ans = []
        cur = []

        def dfs(index):
            if index == len(digits):
                ans.append(cur[:])
                return 
            for c in c_dict[int(digits[index])-int('0')]:
                cur.append(c)
                dfs(index+1)
                cur.pop()

        dfs(0)
        return ans
                
s = Solution()
s.letterCombinations('23')