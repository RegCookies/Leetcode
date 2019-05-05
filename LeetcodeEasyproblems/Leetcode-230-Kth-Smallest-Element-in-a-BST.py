class Solution:
    def rootPath(self,root,k,res):
        if root is None:
            return None 
        
        self.rootPath(root.left,k,res) 
        k[0] -=1 
        if k[0] == 0:
            res[0] = root.val
        
        self.rootPath(root.right,k,res)
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = [-1]
        self.rootPath(root,[k],res)
        return res[0]
