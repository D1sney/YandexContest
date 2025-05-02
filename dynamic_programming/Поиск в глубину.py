import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(graph, visited, now, comp):
    visited[now] = True
    comp.append(now)
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, comp)

n, m = map(int, input().split())
# n и m это обычно количество вершин и ребер в графе
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
comp = []

dfs(graph, visited, 1, comp)
print(len(comp))
print(*sorted(comp))
