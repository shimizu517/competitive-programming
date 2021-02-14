n, x = map(int, input().split())
a = list(map(int, input().split()))

b = [str(item) for item in a if item != x]

if len(b) > 0:
    print(" ".join(b))
else:
    print()
