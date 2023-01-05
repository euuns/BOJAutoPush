studList = []
for i in range(int(input())):
    name,dd,mm,yy = input().split()
    dd,mm,yy = map(int,(dd,mm,yy))
    studList.append([name,dd,mm,yy])

studList.sort(key=lambda x: (x[3],x[2],x[1]))
print(studList[-1][0])
print(studList[0][0])