cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

domain={}
for i in cpdomains:
    count, domains = i.split(" ")
    #print(count,domains)
    sub_domains = domains.split(".")
    
    result = [".".join(sub_domains[i:]) for i in range(len(sub_domains))]
    
    for j in result:
        if j not in domain:
            domain[j] = int(count)
        else:
            domain[j] += int(count)


a = [str(domain[i])+ " " + i for i in domain]
print(a)
