import sys
a_list = []
for i in range(int(sys.stdin.readline())):
    a = list(sys.stdin.readline().split())
    a_list.append(a)

a_list.sort(key=lambda x: int(x[0]))

for i in range(len(a_list)):
    print(a_list[i][0],a_list[i][1])