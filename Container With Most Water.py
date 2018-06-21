def maxArea(height):
    maxarea = 0
    left = 0
    right = len(height) - 1
    while left < right:
        #print(left,right)
        if height[left] <= height[right]:
            #print(left,right,maxarea, height[left]*(right-left))
            maxarea = max(maxarea, height[left]*(right-left))
            left += 1
        else:
            #print(left,right,maxarea, height[left] * (right - left ))
            maxarea = max(maxarea, height[right]*(right-left))
            right -= 1
    return  maxarea

height = [1,8,6,2,5,4,8,3,7]
b = maxArea(height)
print(b)

