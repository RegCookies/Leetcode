class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        stack = []
        stack2 = []
        
        leaf1 = self.findseq(root1,stack)
        leaf2 = self.findseq(root2,stack2)
        return leaf1 == leaf2 
        
    def findseq(self,root,stack): 
        if not root:
            return 
        if root.left is None and root.right is None:
            stack.append(root.val)
        self.findseq(root.left,stack)
        self.findseq(root.right,stack)
        
        return stack
