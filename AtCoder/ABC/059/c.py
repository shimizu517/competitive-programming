def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 10 ** 15

    for i in [-1, 1]:
        ansi, sum = 0, 0
        for a in A:
            print(sum, ansi, i)
            sum += a
            if sum * i <= 0:
                ansi += abs(sum - i)
                sum = i
            i *= -1
        ans = min(ans, ansi)
    print(ans)


main()
