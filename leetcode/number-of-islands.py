class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.n_row = len(grid)
        self.n_col = len(grid[0])
        visited = [[False for _ in range(self.n_col)] for _ in range(self.n_row)]
        result = 0

        for i in range(self.n_row):
            for j in range(self.n_col):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(grid=grid, i=i, j=j, visited=visited)
                    result += 1

        return result

    def dfs(self, grid: List[List[str]], i, j, visited: List[List[bool]]) -> None:
        visited[i][j] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for d1, d2 in directions:
            if d1 == 0 and d2 == 0:
                continue
            # neighboring coordinate
            r, c = i+d1, j+d2
            if r < 0 or self.n_row <= r or c < 0 or self.n_col <= c:
                continue
            if visited[r][c]:
                continue

            if grid[r][c] == '1':
                self.dfs(grid=grid, i=r, j=c, visited=visited)



# Wrong answer.
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         self.n_row = len(grid)
#         self.n_col = len(grid[0])
#         visited = [[False for _ in range(self.n_col)] for _ in range(self.n_row)]
#         result = 0

#         for i in range(self.n_row):
#             for j in range(self.n_col):
#                 if not visited[i][j] and grid[i][j] == '1':
#                     print('dfs')
#                     self.dfs(grid=grid, i=i, j=j, visited=visited)
#                     result += 1

#         return result

#     def dfs(self, grid: List[List[str]], i, j, visited: List[List[bool]]) -> None:
#         print(visited)
#         visited[i][j] = True
#         _direction = [-1, 0, 1]

#         for d1 in _direction:
#             for d2 in _direction:
                  # If I do this, (i+1, j+1) is also checked. This is moved in diagonal way, which is invalid.
#                 if d1 == 0 and d2 == 0:
#                     continue
#                 # neighboring coordinate
#                 r, c = i+d1, j+d2
#                 if r < 0 or self.n_row <= r or c < 0 or self.n_col <= c:
#                     continue
#                 if visited[r][c]:
#                     continue

#                 if grid[r][c] == '1':
#                     self.dfs(grid=grid, i=r, j=c, visited=visited)
