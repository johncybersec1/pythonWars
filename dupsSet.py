def duplicate_or_unique(inList):
    temp = set()  
    dups = set()
    for i in inList:
        if i in temp:
            dups.add(i)
        else:
            temp.add(i)
    if len(dups) == 1:
        for i in dups:
            return i
    s =list(temp - dups)
    for i in s:
        return i