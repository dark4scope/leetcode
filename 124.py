class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val 
        def dfs(root):
            if root == None:
                return 0
            left_side = max(0, dfs(root.left))
            right_side = max(0, dfs(root.right))
            side = max(left_side,right_side)
            self.ans = max([self.ans,left_side+right_side+root.val])
            return side+root.val
        dfs(root)
        return self.ans