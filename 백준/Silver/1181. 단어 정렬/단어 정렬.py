n = int(input())
strList = []
for i in range(n):
    strList.append(input())

li = sorted(set(strList))
li.sort(key=len)

for i in li:
    print(i)