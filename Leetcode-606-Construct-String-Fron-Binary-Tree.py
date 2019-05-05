# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""
        left = self.tree2str(t.left) if t.left else None
        right = self.tree2str(t.right) if t.right else None
        out = str(t.val)
        if left and right:
            out = out + '(' + left + ')' + '(' + right + ')'
        elif left:
            out = out + '(' + left + ')'
        elif right:
            out = out + '()' + '(' + right + ')'
        return out

