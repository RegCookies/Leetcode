def myAtoi(str):
    flag = 1
    str = str.strip()
    if str == "":
        return 0
    if str[0] == "-" or str[0] == "+":
        if str[0] == "-":
            flag = -1
            if str == "-":
                return 0
            else:
                str = str[1:]
        elif str[0] == "+":
            flag = 1
            if str == "+":
                return 0
            else:
                str = str[1:]



    result = ""
    print(str)
    if ord(str[0]) > ord("9") or ord(str[0]) < ord("0"):
        return 0
    else:
        for i in str:
            if ord(i) <= ord("9") and ord(i) >= ord("0"):
                result += i
            else:
                break
        result = flag * int(result)
        print(result)
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if result < -1 * (2 ** 31):
            return -1 * (2 ** 31)
        else:
            return result


a= "-+1"
a = myAtoi(a)
print(a)
print(ord("."))

b = "                  +0   123"
print(b.strip())