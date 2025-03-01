def find_outlier(integers):
    short_lst = list()
    short2_lst = list()
    for i in integers:
        if i%2 == 0:
            short_lst.append(i)
        else:
            short2_lst.append(i)
    print(short_lst)
    print(short2_lst)
    if len(short_lst) > len(short2_lst):
        for i in short2_lst:
            return i
    else:
        for i in short_lst:
            return i

print(find_outlier([2,4,6,8,9]))