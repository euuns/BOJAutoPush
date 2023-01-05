from collections import Counter

number = []
for i in range(int(input())):
    number.append(int(input()))

# 산술평균
print(round(sum(number)/len(number)))

# 중앙값
number.sort()
print(number[(len(number)//2)])

# 최빈값
numCount = Counter(number).most_common()
if len(number) > 1:
    if numCount[0][1] == numCount[1][1]:
        print(numCount[1][0])
    else:
        print(numCount[0][0])
else:
    print(number[0])
    
# 범위
print(max(number)-min(number))