n, k = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
b = [0] * (3 * 10 ** 5)
for i in range(n):
    b[a[i]] += 1


for i in range(n):
    if b[i] == 0:
        break
    if b[i] >= k:
        sum += min(b[i], k)
    else:
        k = b[i]
        if k > 0:
            sum += k
        else:
            break
print(sum)
