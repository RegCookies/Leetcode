
a = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]


def flip(a):
    for i in a:
        for j in range(len(i)):
            if i[j] == 1:
                i[j] =0
            else:
                i[j] =1 
    return a


def reverse_flip(a):
    for i in a:
        for j in range(len(i)):
            index = len(i) - j -1
            if j >= index:
                break
            else:
                i[j],i[index] = i[index],i[j]
    return a

b = reverse_flip(a)
c = flip(b)
print(c)
