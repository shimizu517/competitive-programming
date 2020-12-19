n = int(input())


def has_seven(n) -> bool:
    if "7" in (str(n) + oct(n)):
        return True
    return False


sum = 0
for i in range(1, n + 1):
    if not has_seven(i):
        sum += 1

print(sum)
n = int(input())


def has_seven(n) -> bool:
    if "7" in (str(n) + oct(n)):
        return True
    return False


sum = 0
for i in range(1, n + 1):
    if not has_seven(i):
        sum += 1

print(sum)
提出情報
