def solution(left, right):
    result = 0
    num = [x for x in range(left, right+1)]
    su = []

    for i in range(left, right+1):
        n = []
        for j in range(1, i+1):
            if i%j == 0:
                n.append(j)
        su.append(len(n))

    for i in range(len(su)):
        if su[i]%2 == 0:
            result += num[i]
        else:
            result -= num[i]
    
    return result