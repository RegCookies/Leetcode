# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        d = {}
        def dfs_isCousins(root, par=None, depth=0):
            if root and (x not in d or y not in d):
                d[root.val] = (depth, par)
                dfs_isCousins(root.left, root , depth+1)
                dfs_isCousins(root.right, root, depth+1)
        dfs_isCousins(root)
        
        return d[x][0] == d[y][0] and d[x][1] != d[y][1]
                
            