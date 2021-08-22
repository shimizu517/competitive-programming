# Python program to find
# maximal Bipartite matching.

class GFG:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ppl = len(graph)  # applicantの数
        self.jobs = len(graph[0])  # jobの数

    def bpm(self, u, match_r, visited):
        """
        u(applicant)と隣接する全てのv(job)について、
        """
        for v in range(self.jobs):
            if self.graph[u][v] and not visited[v]:
                visited[v] = True
                # v(job)とマッチングした人がいない、もしくはvとマッチングした人が他のvとマッチングさせられたら、vとuをマッチングさせる
                if match_r[v] == -1 or self.bpm(match_r[v], match_r, visited):
                    match_r[v] = u
                    return True
        return False

    def max_bpm(self):
        match_r = [-1] * self.jobs

        result = 0
        for i in range(self.ppl):

            visited = [False] * self.jobs

            if self.bpm(i, match_r, visited):
                result += 1
        return result


bpGraph = [[0, 1, 1, 0, 0, 0],
           [1, 0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1]]

g = GFG(bpGraph)

print("Maximum number of applicants that can get job is %d " % g.max_bpm())

# This code is contributed by Neelam Yadav
