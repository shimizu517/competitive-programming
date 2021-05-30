n = int(input())
cs = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
ops = []


def mat_mul(A, B):
    rowa = len(A)
    cola = len(A[0])
    colb = len(B[0])
    C = [[0] * colb for _ in range(rowa)]
    for i in range(rowa):
        for j in range(colb):
            for k in range(cola):
                C[i][j] += A[i][k] * B[k][j]
    return C
