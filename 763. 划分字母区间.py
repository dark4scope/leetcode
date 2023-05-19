class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = collections.defaultdict(int)
        ret = []

        # 储存字符的最远下标
        for i in range(len(s)):
            hashmap[s[i]] = max(hashmap[s[i]], i)

        tmp,prev = 0, -1
        for idx, i in enumerate(s):
            tmp = max(tmp, hashmap[i])
            # 如果遍历到的字符等于最远下标，那么这就是一段
            if idx == tmp:             
                ret.append(idx-prev)
                prev = tmp # 更新上一段的坐标

        return ret