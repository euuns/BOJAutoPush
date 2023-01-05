a = [] ; sum = 0
for i in range(int(input())):
    n = int(input())
    if n != 0:
        a.append(n)
    else:
        del a[len(a)-1]

for i in range(len(a)):
    sum += a[i]

print(sum)