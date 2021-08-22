from typing import List


class BPM:
    def __init__(self, edmonds_matrix, X, Y):
        self.edmonds_matrix: List[List[int]] = edmonds_matrix  # edmonds_matrix
        self.X = X  # xの個数
        self.Y = Y  # yの個数

    def dfs(self, s, matched_pair: List[int], visited: List[bool]):
        for y in range(self.Y):
            if self.edmonds_matrix[s][y] != 0 and not visited[y]:
                visited[y] = True
                if matched_pair[y] == -1 or self.dfs(s=matched_pair[y], matched_pair=matched_pair, visited=visited):
                    matched_pair[y] = s
                    return True
        return False

    def execute(self):
        matched_pair = [-1] * self.Y  # matched_pair[i] = yiとマッチしたxj
        result = 0
        for i in range(self.X):
            visited = [False] * self.Y
            if self.dfs(s=i, matched_pair=matched_pair, visited=visited):
                result += 1
        return result


def main():
    X, Y, E = map(int, input().split())
    edmonds_matrix = [[0] * Y for _ in range(X)]  # edmonds_matrix
    for _ in range(E):
        x, y = map(int, input().split())
        edmonds_matrix[x][y] = 1
    print(BPM(edmonds_matrix=edmonds_matrix, X=X, Y=Y).execute())


main()
