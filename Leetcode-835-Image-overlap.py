A = [[1,1,0],
     [0,1,0],
     [0,1,0]]

B = [[0,0,0],
     [0,1,1],
     [0,0,1]]
import collections
def large(A,B):
    N = len(A) 
    LA = [(xi, yi) for xi in range(N) for yi in range(N) if A[xi][yi]]
    LB = [(xi, yi) for xi in range(N) for yi in range(N) if B[xi][yi]]
    print(LA,LB)
    
    d = collections.Counter([(x1-x2,y1-y2) for (x1,y1) in LA for (x2,y2) in LB])
    print(d)
    return max(d.values() or [0])

print(large(A,B))
