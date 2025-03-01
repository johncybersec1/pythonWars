def solution(number):
    toSum = list()
    for num in range(number):
        if number == -1 or number == 0:
            return 0
        if (num)%3 == 0 or (num)%5 == 0:
            toSum.append(num)
            print(toSum)
        elif (num)%3 == 0 and (num)%5 == 0:
            toSum.append(num)
        else:
            continue
    print(toSum)
    return sum(toSum)

print(solution(16))

#What I learnt is that using a list can limit the buffer size for your computation.