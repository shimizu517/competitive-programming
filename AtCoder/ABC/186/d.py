from functools import reduce

n = int(input())
a = [v for v in map(int, input().split())]

a.sort()

sum = 0
last_add = 0
for i in range(1, len(a)):
    diff = a[i] - a[i - 1]
    last_add += i * diff
    sum += last_add

print(sum)
