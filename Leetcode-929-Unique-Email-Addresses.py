import re

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

result = set()

for e in emails:
    word = e.split("@")
    #print(word)
    front = word[0]
    back = word[1]
    #print(front)
    front = re.sub("\+.*",'', front)
    #print(front)
    front = re.sub("\.", "", front)
    #print(front)

    full_add = front + "@" + back

    result.add(full_add)

print(result)
