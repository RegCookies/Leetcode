class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r,s = 0,0
        for i,v in enumerate(grid):
            for j,v in enumerate(v):
                if v:
                    r += 4*v+2
                    s +=min(v,grid[i-1][j]) if i else 0
                    s +=min(v,grid[i][j-1]) if j else 0 
        return r - 2*s;
