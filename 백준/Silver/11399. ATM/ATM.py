n = int(input())
p = list(map(int, input().split()))
p.sort() ; result = [] ; sum = 0
for i in range(n):
    if i == 0:
        result.append(p[i])
    else:
        result.append(result[i-1]+p[i])
    sum += result[i]
print(sum)