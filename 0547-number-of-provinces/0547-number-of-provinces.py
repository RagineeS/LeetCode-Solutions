class Solution:
    def dfs(self, node, isConnected, visited):
        visited[node] = True
        for i in range(len(isConnected)):
            if not visited[i] and isConnected[node][i] == 1:
                self.dfs(i, isConnected, visited)
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(i, isConnected, visited)
                provinces += 1
        return provinces