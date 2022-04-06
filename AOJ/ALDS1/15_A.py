def solve(n: int):
    count = 0
    for coin in [25, 10, 5, 1]:
        count += n // coin
        n %= coin
    print(count)


def main():
    n = int(input())
    solve(n)


main()
