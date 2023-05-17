class Solution(object):
    def subsetsWithDup(self, nums):
        res, path = [], []
        self.dfs(nums, 0, res, path)
        return res
    
    def dfs(self, nums, index, res, path):
        res.append(copy.deepcopy(path))
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, res, path)
            path.pop()

# 回溯具有两种遍历方法，一种是在当前位置遍历后续所有可能的位置，一种是直接懒操作，选择该位置、或者不选择该位置
# 这里选择第一种方法可以去重

