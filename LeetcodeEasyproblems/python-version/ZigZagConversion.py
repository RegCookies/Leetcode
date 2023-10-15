def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if s == "":
        return ""
    elif len(s) == 1 or numRows == 1:
        return s
    else:
        step = 2 * numRows - 1
        table = [[] for i in range(numRows)]
        result = ""
        for i in range(0, len(s), step - 1):
            k = i
            # in each step
            for j in range(k, min(k + step - 1, len(s))):
                # print(k,k+step-1,j,s[j])
                if j <= k + numRows - 1:
                    table[j - k].append(s[j])
                else:
                    table[2 * numRows - j + k - 2].append(s[j])

        for i in table:
            for j in i:
                result += j
        return result


s = "PAYPALISHIRING"
a = convert(s, 4)
print(a)