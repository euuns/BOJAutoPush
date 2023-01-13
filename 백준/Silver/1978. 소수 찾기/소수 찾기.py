n = int(input())
a = list(map(int,input().split()))
count = 0

def prime(num):
    global count
    if num == 1:
        return
    else:
        for i in range(2,num+1):
            if i == num:
                count += 1
            if num%i == 0:
                break

for i in range(len(a)):
    prime(a[i])

print(count)