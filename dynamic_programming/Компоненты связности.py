
def dfs(graph, visited, now):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig)

def find_components():
    N, M = map(int, input().split())
    graph = list(map(int, input().split()))

    visited = []
    comp = 1
    comp_list = []
    for now in graph:
        if graph in visited:
            continue
        dfs(graph, visited, now)
        comp_list.append()
        comp +=1
        comp_list



