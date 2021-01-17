q = int(input())

xys = []
for i in range(q):
    x = input()
    y = input()
    xys.append({"x": x, "y": y})


def lcs_length(X, Y):
    c = [[0] * (len(X) + 1) for _ in range((len(Y) + 1))]
    for j in range(len(Y)):
        for i in range(len(X)):
            if X[i] == Y[j]:
                c[j + 1][i + 1] = c[j][i] + 1
            else:
                c[j + 1][i + 1] = max(c[j][i + 1], c[j + 1][i])
    return c[len(Y)][len(X)]


for xy in xys:
    print(lcs_length(xy["x"], xy["y"]))
