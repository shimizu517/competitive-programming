n, m = map(int, input().split())
ab = []
for _ in range(m):
    ab.append(list(map(int, input().split())))

k = int(input())
cd = []
for _ in range(k):
    cd.append(list(map(int, input().split())))

all_patterns = []

max_s = 0
for i in range(2 ** k):
    sum = 0
    indice = bin(i)[2:].zfill(k)
    l = [cd[i][int(c)] for i, c in enumerate(indice)]
    for item in ab:
        if item[0] in l and item[1] in l:
            sum += 1
    max_s = max(sum, max_s)

print(max_s)
