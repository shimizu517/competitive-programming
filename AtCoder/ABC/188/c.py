import copy

N = int(input())
A = list(map(int, input().split()))

B = [i for i in range(2 ** (N))]

for i in range(N):
    C = []
    # print('B',B)
    for j in range(2 ** (N - i - 1)):
        # if i == N - 1:
        if len(B) == 2:
            print(B[2 * j] + 2) if A[B[2 * j]] > A[B[2 * j + 1]] else print(
                B[2 * j] + 1
            )
        else:
            C.append(B[2 * j]) if A[B[2 * j]] > A[B[2 * j + 1]] else C.append(
                B[2 * j + 1]
            )
    B = copy.deepcopy(C)
