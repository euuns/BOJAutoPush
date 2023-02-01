import sys

N = int(sys.stdin.readline())
stack = []
result = []

for i in range(N):
    now = sys.stdin.readline().split()

    if len(now) == 2:
        stack.append(int(now[1]))

    elif now == ['pop']:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    
    elif now == ['size']:
        print(len(stack))
    
    elif now == ['empty']:
        if not stack:
            print(1)
        else:
            print(0)
    
    elif now == ['top']:
        if not stack:
            print(-1)
        else:
            print(stack[-1])