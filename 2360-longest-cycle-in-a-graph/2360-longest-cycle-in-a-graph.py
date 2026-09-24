class Solution:
    def dfs(self, u, edges, visited, dist, inRecursion):
        if u != -1:
            visited[u] = True
            inRecursion[u] = True
            v = edges[u]

            if v != -1 and not visited[v]:
                dist[v] = dist[u] + 1
                self.dfs(v, edges, visited, dist, inRecursion)
            elif v != -1 and inRecursion[v]:
                self.result = max(self.result, dist[u] - dist[v] + 1)

            inRecursion[u] = False

    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        visited = [False] * n
        dist = [1] * n
        inRecursion = [False] * n
        self.result = -1

        for i in range(n):
            if not visited[i]:
                self.dfs(i, edges, visited, dist, inRecursion)

        return self.result