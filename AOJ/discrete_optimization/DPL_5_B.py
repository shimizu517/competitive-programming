from math import factorial

n, k = map(int, input().split())

if n > k:
    print(0)
else:
    print(pow(int(factorial(k) // factorial(k - n)), 1, 10 ** 9 + 7))
    # これだとWAになった。print(pow(int(factorial(k) / factorial(k - n)), 1, 10 ** 9 + 7))
