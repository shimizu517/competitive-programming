from typing import List


def matrix_chain_multiplication(matrices: List[List[int]], dp, s, t):
    if dp[s][t] != -1:
        return dp[s][t]
    dp[s][t] = 10 ** 7
    for i in range(s, t):
        result = (matrix_chain_multiplication(matrices=matrices, dp=dp, s=s, t=i)
                  + matrix_chain_multiplication(matrices=matrices, dp=dp, s=i + 1, t=t)
                  + matrices[s][0] * matrices[i][1] * matrices[t][1])
        dp[s][t] = min(result, dp[s][t])
    return dp[s][t]


def main():
    n = int(input())
    matrices = []
    for _ in range(n):
        matrices.append(list(map(int, input().split())))
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    print(matrix_chain_multiplication(matrices=matrices, dp=dp, s=0, t=n - 1))


main()
