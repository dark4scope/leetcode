from collections import Counter
from heapq import heapify, heappushpop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 方法二：哈希+最小堆
        # 时间复杂度：O(nlogk)
        cnt = Counter(nums)
        l = list(zip(cnt.values(),cnt.keys()))
        hp = l[:k]
        heapify(hp)
        for item in l[k:]:
            heappushpop(hp,item)
        return [item[1] for item in hp]