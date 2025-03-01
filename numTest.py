def fix_progression(arr):
    temp = set()
    if len(arr) <= 2:
        return 0
    for i in range(len(arr) - 1):
        diff = arr[i] - arr[i+1]
        temp.add(diff)
        print(temp)
    if len(temp) == 1:
        return 0
    else:
        temp.pop()
    return (len(temp) - 1)

arr = [7,7,7,7,8,7,7,7]

print(fix_progression(arr))