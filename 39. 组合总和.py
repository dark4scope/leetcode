from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        candidates.sort(reverse=True)

        def dfs(index, target):
            if target == 0:
                ans.append(cur[:])
                return
            else:
                for i in range(index, len(candidates)):
                    if candidates[i] <= target:
                        cur.append(candidates[i])
                        dfs(i, target-candidates[i])
                        cur.pop()
        dfs(0,target)

        return ans


s = Solution()
s.combinationSum([5,3],8)