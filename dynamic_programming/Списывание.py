import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(graph, visited, now):

    for neig in graph[now]:
        if visited[neig] == 0:
            # красим соседа в «другой» цвет: 3 - текущий
            visited[neig] = 3 - visited[now]
            if not dfs(graph, visited, neig):
                return False
        elif visited[neig] == visited[now]:
            # сосед того же цвета — двудольность нарушена
            return False
    # если ни в одном из соседей конфликта не нашли
    return True

n, m = map(int, input().split())
# n и m это обычно количество вершин и ребер в графе
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [0] * (n+1)

for now in range(1, n+1):
    if visited[now] == 0:
        visited[now] = 1
        if not dfs(graph, visited, now):
            print('NO')
            sys.exit()

print('YES')
