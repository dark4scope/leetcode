# 这个题是真的很好啊，这种管理数据的思想很妙
import heapq


class ExamRoom:

    def __init__(self, N: int):
        self.n = N
        self.heap = []
        self.pairs = {}
        self.add(0, N)

    def add(self, left, right):
        if left == 0 or right == self.n:
            distance = right - left
        else:
            distance = (right - left + 1) >> 1

        heapq.heappush(self.heap, (-distance, left, right))
        self.pairs[left] = right
        self.pairs[right] = left

    def seat(self) -> int:
        left = right = -1
        while self.heap:  # check for lasy deletion
            _, left, right = heapq.heappop(self.heap)
            if left == self.pairs.get(right, -1) and right == self.pairs.get(left, -1): # 左右区间在区间对中都找到,延迟删除距离较大的区间
                break

        if left == 0:
            p = 0
        elif right == self.n:
            p = self.n - 1
        else:
            p = (left + right - 1) >> 1

        self.add(left, p)
        self.add(p + 1, right)
        return p

    def leave(self, p: int) -> None:
        left = self.pairs.pop(p)
        right = self.pairs.pop(p + 1)
        self.add(left, right)
