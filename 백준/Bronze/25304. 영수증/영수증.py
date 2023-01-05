total = 0
sum = int(input())
number = int(input())

for i in range(number):
    a, b = map(int,input().split())
    total += a*b

if sum==total:
    print("Yes")
else:
    print("No")