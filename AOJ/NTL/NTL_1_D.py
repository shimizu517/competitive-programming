def totient(n: int):
    result = n
    x = 2
    while x ** 2 < n:
        if n % x == 0:
            result = result // x * (x - 1)
            while n % x == 0:
                n //= x
        x += 1
    if n > 1:
        result = result // n * (n - 1)
    return result


def main():
    n = int(input())
    print(totient(n=n))


main()
