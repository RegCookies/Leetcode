grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

#find the top to bottom grid
left_right = []
for i in grid:
    left_right.append(max(i))
top_down = []

for i in range(len(grid)):
    max_num = 0
    for j in range(len(grid[i])):
        if grid[j][i] >= max_num:
            max_num = grid[j][i]
    top_down.append(max_num)

#deal with increase

count = 0

for i in range(len(grid)): 
    for j in range(len(grid[i])):
        if grid[i][j] <= min(left_right[i],top_down[j]):
            count += min(left_right[i],top_down[j]) - grid[i][j]

print(left_right)
print(top_down)
print(count)

