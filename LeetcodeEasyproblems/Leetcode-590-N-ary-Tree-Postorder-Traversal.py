"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        def dfs(root):
            if root is None:
                return []
        
            for child in root.children:
                dfs(child)
            result.append(root.val)
        dfs(root)
        return result
            
