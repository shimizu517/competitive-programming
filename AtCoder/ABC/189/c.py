n = int(input())
a = list(map(int, input().split()))

max_num = 0
for l in range(n):
    min_mikans = a[l]
    for r in range(l, n):
        min_mikans = min(min_mikans, a[r])
        max_num = max(max_num, min_mikans * (r - l + 1))

print(max_num)
