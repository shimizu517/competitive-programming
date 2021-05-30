import math

x, y, r = map(lambda x: float(x) * 10000, input().split())

maxy = math.floor((y ** 0.0001 + r ** 0.0001)) * 10000
miny = math.ceil((y ** 0.0001 - r ** 0.0001)) * 10000

result = 0
for cy in range(miny, maxy + 10000, 10000):
    left = x - (r ** 2 - (cy - y) ** 2) ** 0.5
    right = x + (r ** 2 - (cy - y) ** 2) ** 0.5
    result += math.floor(right // 10000) - math.ceil(left // 10000) + 1

print(result)
