def main():
    N = int(input())
    D = [int(input()) for i in range(N)]
    print(len(list(set(D))))


main()
