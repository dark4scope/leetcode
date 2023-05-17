from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        ans = 0
    
        cur_sum = 0
        for n in nums:
            cur_sum += n
            ans += d[cur_sum-k]
            d[cur_sum] += 1
        return ans