class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1] * len(ratings)
        right = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1
        for i in range(len(ratings)-2, -1, -1):
            print(i)
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 1
        return sum(max(i,j) for i,j in zip(left,right))