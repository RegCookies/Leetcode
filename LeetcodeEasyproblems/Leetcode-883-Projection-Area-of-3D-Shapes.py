grid = [[1,1,1],[1,0,1],[1,1,1]]

col_max =  [0 for i in range(len(grid))]
bottom_area =  0
for i in range(len(grid)):
    row_max = 0
    for j in range(len(grid[i])):
        if grid[i][j] != 0:
            bottom_area += 1
        if grid[i][j] > row_max:
            row_max = grid[i][j]
        if grid[i][j] > col_max[j]:
            col_max[j] = grid[i][j]
            print(col_max)
    bottom_area += row_max
print(col_max)
print(bottom_area + sum(col_max))
