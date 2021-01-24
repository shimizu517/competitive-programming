n = int(input())
s = [None]
for _ in range(n):
    s.append(input())


def num(i):
    if i == 0:
        return 1
    elif s[i] == 'AND':
        return num(i - 1)
    else:
        return 2 ** i + num(i - 1)


print(num(n))
