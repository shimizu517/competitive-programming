# from collections import deque
#
# INF = 1 << 30
#
# N, M = map(int, input().split())
# g = [[] for _ in range(N)]
# for i in range(M):
#     A, B = map(int, input().split())
#     A -= 1
#     B -= 1
#     g[A].append(B)
#     g[B].append(A)
#
# K = int(input())
# C = list(map(int, input().split()))
# for i in range(K):
#     C[i] -= 1
#
#
# def BFS(s):
#     cost = [INF] * N
#     cost[s] = 0
#     q = deque([s])
#     while q:
#         x = q.popleft()
#         for y in g[x]:
#             if cost[y] == INF:
#                 cost[y] = cost[x] + 1
#                 q.append(y)
#     return [cost[c] for c in C]
#
#
# cost = [BFS(c) for c in C]
#
# dp = [[INF] * K for i in range(1 << K)]
# for i in range(K):
#     dp[1 << i][i] = 1
#
# for bit in range(1 << K):
#     for i in range(K):
#         if dp[bit][i] == INF:
#             continue
#         for j in range(K):
#             if bit & 1 << j:
#                 continue
#             if dp[bit ^ 1 << j][j] > dp[bit][i] + cost[i][j]:
#                 dp[bit ^ 1 << j][j] = dp[bit][i] + cost[i][j]
#
# ans = min(dp[-1])
# if ans == INF:
#     ans = -1
# print(ans)
#

a = [1, 5, 2, 9]
for i in range(1 << len(a)):
    result = []
    for j in range(len(a)):
        if i & 1 << j:
            result.append(a[j])
    print(result)
