# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """ 
        if not root:
            return [root]
        res = []
        queue = [root]
        while(queue):
            length = len(queue)
            cSum = 0
            for _ in range(length):
                node = queue.pop(0)
                cSum += node.val
                if(node.left != None):
                    queue.append(node.left)
                if(node.right != None):
                    queue.append(node.right)
            res.append(cSum / length)
        return res
        
