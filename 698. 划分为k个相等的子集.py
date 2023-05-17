class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        @cache
        def dfs(state, t):
            if state == mask:
                return True
            for i, v in enumerate(nums):
                if (state >> i) & 1: 
                    continue
                if t + v > s:
                    break
                if dfs(state | 1 << i, (t + v) % s):
                    return True
            return False

        s, mod = divmod(sum(nums), k)
        if mod:
            return False
        nums.sort()
        mask = (1 << len(nums)) - 1
        return dfs(0, 0)
    

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    all = sum(nums)
    if all % k:
        return False
    per = all // k
    nums.sort()  # 方便下面剪枝
    if nums[-1] > per:
        return False
    n = len(nums)

    @cache
    def dfs(s, p):
        if s == 0:
            return True
        for i in range(n):
            if nums[i] + p > per:
                break
            if s >> i & 1 and dfs(s ^ (1 << i), (p + nums[i]) % per):  # p + nums[i] 等于 per 时置为 0  s >> i & 1 第个位置的数字还在， s ^ (1 << i) 为取走第i个数字
                return True
        return False
    return dfs((1 << n) - 1, 0)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 倒序排序,在后面if bucket[i] + nums[curr] > aver 能更快的判断是否不可能满足要求
        nums.sort(reverse=True)

        tot = sum(nums)
        aver = tot//k
        # 无法平均
        if tot%k!=0:
            return False
        # 最大值大于平均值,不可能平均
        if nums[-1] > aver:
            return False

        # k个桶
        bucket = [0]*k
        def back(curr,bucket):
            # print(bucket)
            """
            为什么不会出现有桶值小于aver,但是n个值都已经全部添加进桶的情况?
                答:有小值出现,那么一定会有大值出现,才能造成平均分配,
                但是我们用bucket[i] + nums[curr] > aver
                限制了大值的出现,所以桶内的值一定是平均值
            """
            # 表示n个值都已经全部添加进桶,再加上前面已经判断总值可以被平均分配,所以成功划分
            if curr==len(nums):
                return True
            for i in range(k):
                # 不可能满足要求,跳过
                if bucket[i] + nums[curr] > aver:
                    continue
                # 如果上一个桶值与当前桶值相同,则添加的结果也上一个桶相同
                if i>0 and bucket[i]==bucket[i-1]:
                    continue
                bucket[i] += nums[curr]
                if back(curr+1,bucket):
                    return True
                bucket[i] -= nums[curr]
            return False
        return back(0,bucket)