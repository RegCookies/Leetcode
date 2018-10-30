
S = "loveleetcode"
C = "e"
    

closest = float('-inf')
res = []
for i, char in enumerate(S):
    if char == C: closest = i
    print(i,closest,i-closest)
    res.append(i - closest)

closest = float('inf')
for i in range(len(S) -1, -1, -1):
    if S[i] == C: closest = i
    res[i] = min(res[i], closest - i)
print(res)
    
