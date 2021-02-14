N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * N
c[0] = a[0] * b[0]

print(c[0])
for i in range(1, N):
    a[i] = max(a[i - 1], a[i])
    c[i] = max(c[i - 1], a[i] * b[i])
    print(c[i])

# TLE
# for j in range(1, N):
#     _max = c[j - 1]
#     for i in range(j + 1):
#         _max = max(_max, a[i] * b[j])
#     c[j] = _max
#     print(c[j])
