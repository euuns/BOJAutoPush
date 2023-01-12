T = int(input())
R_list = [] ; S_list = []
for i in range(T):
    R, S = input().split()
    R_list.append(int(R))
    S_list.append(list(S))

for i in range(T):
    for j in range(len(S_list[i])):
        print(S_list[i][j]*R_list[i], end='')
    print(end='\n')