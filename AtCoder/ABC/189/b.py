n, x = map(int, input().split())

vp: [[int]] = []

sum = 0
is_done = False

for i in range(n):
    v, p = map(int, input().split())
    sum += v * p
    if sum > x * 100:
        print(i + 1)
        is_done = True
        break

if not is_done:
    print(-1)
