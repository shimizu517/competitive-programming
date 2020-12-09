def main():
    N, Y = map(int, input().split())
    for i in range(0, N + 1):
        for j in range(0, N - i + 1):
            k = N - j - i
            if i * 10000 + j * 5000 + k * 1000 == Y:
                print(f"{i} {j} {k}")
                return
    print("-1 -1 -1")


main()
