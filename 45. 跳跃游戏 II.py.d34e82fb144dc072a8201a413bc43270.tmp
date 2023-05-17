class Solution:
    def jump(self, nums: List[int]) -> int:
        maxvalue =0
        end = 0
        n = len(nums)
        step = 0
        for i in range(n-1):
            if maxvalue>=i:
                maxvalue = max(maxvalue,i+nums[i])
            if i==end:
                end = maxvalue
                step+=1
        return step