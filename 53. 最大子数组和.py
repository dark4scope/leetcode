class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = cur_sum = nums[0]

        for n in nums[1:]:
            cur_sum = max(cur_sum+n, n)
            ans = max(cur_sum, ans)
        return ans