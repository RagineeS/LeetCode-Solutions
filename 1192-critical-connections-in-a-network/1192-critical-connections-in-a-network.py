class Solution:
    def criticalConnections(self,n,connections):
        adj=[[] for _ in range(n)]
        tin=[-1]*n
        low=[-1]*n
        bridges=[]
        timer=0

        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node,parent):
            nonlocal timer
            tin[node]=low[node]=timer
            timer+=1

            for nei in adj[node]:
                if nei==parent:
                    continue

                if tin[nei]!=-1:
                    low[node]=min(low[node],tin[nei])
                else:
                    dfs(nei,node)
                    low[node]=min(low[node],low[nei])

                    if low[nei]>tin[node]:
                        bridges.append([node,nei])

        for i in range(n):
            if tin[i]==-1:
                dfs(i,-1)

        return bridges