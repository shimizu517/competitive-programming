def main():
    h, w = map(int, input().split())

    s = []
    for i in range(h):
        s.append(input())

    result = 0
    for i in range(h - 1):
        for j in range(w - 1):
            rec = [s[i][j], s[i][j + 1], s[i + 1][j], s[i + 1][j + 1]]
            if rec.count('#') == 1 or rec.count('#') == 3:
                result += 1

    print(result)


main()
