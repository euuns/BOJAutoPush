number = int(input())
count = number
for i in range(number):
    a = input()
    for j in range(len(a)-1):
        if a[j] != a[j+1]:
            if a[j] in a[j+1:]:
                count -= 1
                break

print(count)