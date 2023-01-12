A, B = map(int, input().split())
A = list(map(int, str(A))) 
B = list(map(int, str(B)))

a = 0
for i in range(len(A)):
    a = a*10 + A.pop()
b = 0
for i in range(len(B)):
    b = b*10 + B.pop()

if a > b:
    print(a)
else:
    print(b)