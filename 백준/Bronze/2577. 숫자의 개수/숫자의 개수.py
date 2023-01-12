A = int(input())
B = int(input())
C = int(input())
mul = A*B*C
a = [int(a) for a in str(mul)]

for i in range(10):
    print(a.count(i))