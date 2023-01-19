T = int(input())
result = []
for i in range(T):
    data = input()

    flag = False
    stack = []

    for i in data:
        if not stack and i==')':
            flag = True
            break
        elif i == '(':
            stack.append(i)
        else:
            stack.pop()
    
    if stack:
        flag = True
    
    result.append(flag)
        

    
for i in range(T):
    if result[i]:
        print('NO')
    else:
        print('YES')