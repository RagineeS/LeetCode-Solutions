class Solution:
    def dfs(self, adj, start, temp, result):
        if start == self.target:
            result.append(temp[:])
            return
        for x in adj[start]:
            temp.append(x)
            self.dfs(adj, x, temp, result)
            temp.pop()
    def allPathsSourceTarget(self, graph):
        result = []
        temp = [0]
        self.target = len(graph) - 1
        self.dfs(graph, 0, temp, result)
        return result