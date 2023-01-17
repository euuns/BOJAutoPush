import sys

r = 31
M = 1234567891
result = 0
l = int(input())

def hash_func(key,i):
    return (key*(r**i)) % M

def setNum(n):
    return int(ord(n))-96

li = list(map(str, sys.stdin.readline().strip()))
alpa = [setNum(x) for x in li]


for i in range(l):
    result += hash_func(alpa[i],i)

print(result)