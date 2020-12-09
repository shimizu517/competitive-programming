def draw_black(rect: list, v: int):
    for ri in range(len(rect)):
        for ci in range(len(rect[ri])):
            if v[2] == 1:
                condition = ci < v[0]
            elif v[2] == 2:
                condition = ci > v[0] - 1
            elif v[2] == 3:
                condition = ri < v[1]
            else:
                condition = ri > v[1] - 1
            if condition:
                rect[ri][ci] = 1


def main():
    W, H, N = list(map(int, input().split()))
    vs = []
    for _ in range(N):
        vs.append(list(map(int, input().split())))

    rect = [[0] * W for _ in range(H)]
    for v in vs:
        draw_black(rect, v)

    result = W * H
    for r in rect:
        for c in r:
            result -= c
    print(result)


main()
