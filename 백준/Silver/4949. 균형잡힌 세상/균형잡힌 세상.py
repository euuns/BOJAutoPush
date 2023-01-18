result = []
while True:
    s = input()
    if s == '.':
        break
    
    stack = []
    flag = False

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack.pop() != '('  :
                flag = True
                break
        elif i == ']':
            if not stack or stack.pop() != '[':
                flag = True
                break
        
    if stack:
        flag = True
        
    result.append(flag)

for i in range(len(result)):
    if result[i]:
        print('no')
    else:
        print('yes')