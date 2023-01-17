import sys

n = int(input())    # 입력 받을 수열
stack = []          # stack 형태로 진행될 수열을 담을 리스트
result = []         # pop, push의 순서를 저장할 리스트
flag = False        # flag가 True인 경우, 연산 불가능 == NO 출력
cnt = 1             # 1부터 n까지 오름차순으로 진행하기 위한 변수

for i in range(n):
    x = int(sys.stdin.readline())

    # 입력받은 x만큼 stack에 push하기 위한 반복문
    while cnt <= x:
        stack.append(cnt)
        cnt += 1
        result.append('+')
    
    # x가 stack의 제일 마지막과 같은 값일 때 pop
    if stack[-1] == x:
        result.append('-')
        stack.pop()
    else:
        # stack에 더 이상 남아 있는 수가 없어 연산이 불가능
        flag = True

if flag:
    print('NO')
else:
    for i in result:
        print(i)