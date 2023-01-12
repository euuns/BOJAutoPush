n = int(input())
a = list(map(int, input().split()))
sumlist = []
for i in a:
    sumlist.append(i/max(a)*100)
print(sum(sumlist)/n)