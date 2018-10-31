d = dict()
        for i in A:
            if len(i) >= 2:
                key = (tuple(sorted(i[::2])), tuple(sorted(i[1::2])))
                d[key] = d.get(key,0) + 1
            else:
                d[i] = d.get(i,0) + 1     
        return len(d) 
