h, w = map(int, input().split())
a = []
minimum = 100
for i in range(h):
    row = list(map(int, input().split()))
    minimum = min(*row, minimum)
    a.extend(row)

sum = 0
for item in a:
    sum += item - minimum

print(sum)
