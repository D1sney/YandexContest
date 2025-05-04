import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    # Ссылки «круговых» соседей
    nxt = [(i+1) % n for i in range(n)]
    prv = [(i-1) % n for i in range(n)]
    ans = [0]*n
    alive = n

    # Инициализационная очередь раунда 1
    from collections import deque
    curr = deque()
    for i in range(n):
        if n >= 3 and a[i] < a[prv[i]] and a[i] < a[nxt[i]]:
            curr.append(i)

    round_num = 1
    # Множество кандидатов-соседей на следующий раунд
    while curr and alive > 2:
        # удаляем всех в curr
        next_candidates = set()
        for i in curr:
            if ans[i] != 0:
                continue  # на всякий случай
            ans[i] = round_num
            # «вырезаем» i из круга
            L, R = prv[i], nxt[i]
            nxt[L] = R
            prv[R] = L
            alive -= 1
            next_candidates.add(L)
            next_candidates.add(R)
        # готовим список для следующего раунда
        curr = deque()
        for j in next_candidates:
            if ans[j] == 0 and alive > 2:
                # обновлённые соседи после удаления всех i
                if a[j] < a[prv[j]] and a[j] < a[nxt[j]]:
                    curr.append(j)
        round_num += 1

    # Вывод
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
