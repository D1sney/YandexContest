import sys
sys.setrecursionlimit(300000)   # 1) Поднимаем лимит рекурсии, чтобы стек не переполнялся при глубине до ~100000
input = sys.stdin.readline       # 2) Быстрый ввод строк (важно при N, M до 10^5)

def dfs(graph, visited, now, comp):
    # now — текущая вершина, в которую мы зашли
    # comp — список, куда мы будем добавлять все вершины этой компоненты связности

    visited[now] = True    # 3) отмечаем: в эту вершину мы уже заходили
    comp.append(now)       # 4) запоминаем её в списке текущей компоненты

    for neig in graph[now]:   # 5) пробегаем всех соседей
        if not visited[neig]:
            dfs(graph, visited, neig, comp) # 6) рекурсивно спускаемся в не посещённую смежную вершину

def main():
    n, m = map(int, input().split())     # 7) читаем N, M
    graph = [[] for _ in range(n+1)]     # 8) создаём пустой список смежности для 1..n

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)               # 9) добавляем ребро u→v
        graph[v].append(u)               # 10) и v→u, т.к. граф неориентированный

    visited = [False] * (n+1)            # 11) массив меток посещённых вершин
    components = []                      # 12) итоговый список компонент

    # 13) перебираем все вершины; если какая-то ещё не посещена — запускаем DFS
    for v in range(1, n+1):
        if not visited[v]:
            comp = []         # 14) заводим новый список для текущей компоненты
            dfs(graph, visited, v, comp)      # 15) заполняем его всеми достижимыми из v вершинами
            components.append(comp)

    # 16) выводим результат
    print(len(components))
    for comp in components:
        print(len(comp))
        print(*comp)

if __name__ == "__main__":
    main()
