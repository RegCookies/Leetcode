class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root or root.val == val:
            return root 
        
        return self.searchBST(root.left,val) if root.val > val else self.searchBST(root.right,val)
