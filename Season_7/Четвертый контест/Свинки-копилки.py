import sys

def main():
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    n = int(input())
    f = [0] * (n + 1)
    for i in range(1, n+1):
        f[i] = int(input())

    visited = [0] * (n + 1)  # 0 — не тронут, 1 — в текущем обходе, 2 — полностью обработан
    cycles = 0

    for i in range(1, n+1):
        if visited[i] != 0:
            continue
        j = i
        # идём по стрелкам, пока не встретим уже посещённую вершину
        while visited[j] == 0:
            visited[j] = 1
            j = f[j]
        # если она в текущем стеке — нашли новый цикл
        if visited[j] == 1:
            cycles += 1
        # теперь «снимаем метки» 1 → 2 для всех, кто был в этом обходе
        k = i
        while visited[k] == 1:
            visited[k] = 2
            k = f[k]

    print(cycles)


if __name__ == "__main__":
    main()
