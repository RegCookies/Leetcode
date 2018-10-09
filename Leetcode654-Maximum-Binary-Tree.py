class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums :
            return
        if len(nums) ==1 :
            return TreeNode(nums[0]) 
        
        val = max(nums)
        i = nums.index(val)
        
        root = TreeNode(val)
    
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i+1:])
        
        return root
