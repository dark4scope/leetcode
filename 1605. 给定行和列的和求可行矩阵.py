class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res=[[0]*len(colSum) for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                tmp=min(rowSum[i],colSum[j])
                res[i][j]=tmp
                rowSum[i]-=tmp
                colSum[j]-=tmp
        return res
