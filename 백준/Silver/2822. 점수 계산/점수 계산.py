a = []
for i in range(8):
    score = int(input())
    a.append(list(map(int, (i+1, score))))
a.sort(key=lambda x:x[1],reverse=True)

sum = 0 ; sumlist = []
for i in range(5):
    sum += a[i][1]
    sumlist.append(a[i][0])
sumlist.sort()

print(sum)
for i in range(len(sumlist)):
    print(sumlist[i],end=' ')