s1 = "db"
s2 = "b"
s3 = "cbb"


def isInterLeave(s1,s2,s3):
    if s1 == "":
        return s3 == s2
    if s2 == "":
        return s3 == s1
    if s3 == "":
        return s1 == s2 == ""
    if len(s3) != len(s1) + len(s2): return False


    #dp = [[True for i in range(len(s1)+1)] for j in range(len(s2)+1)]
    dp = [[True]*(len(s2)+1)for j in range(len(s1)+1)]
    print(dp)

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i or j: 
                print(i,j,s1[i-1:i],s2[j-1:j],s3[i+j-1] )
                dp[i][j] = (s1[i-1:i] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1:j]== s3[i+j-1] and dp[i][j-1])
    

    return dp[-1][-1]

a = isInterLeave(s1,s2,s3)

print(a)
