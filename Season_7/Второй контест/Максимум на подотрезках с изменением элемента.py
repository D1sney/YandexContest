
def max_with_update():
    import sys
    input = sys.stdin.readline

    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())

    # 1) размер под дерево
    s = 1
    while s < n:
        s *= 2

    # 2) массив-дерево
    tree = [0] * (2 * s)

    # 3) заполняем листья, кладем индекс i + 1
    for i in range(n):
        tree[s + i] = (nums[i])
    # от s+n до 2s-1 уже (0)

    # 4) строим внутренние
    for i in range(s - 1, 0, -1):
        tree[i] = max(tree[2*i], tree[2*i + 1])

    # 5) рекурсивный запрос
    def query(node, L, R, ql, qr):
        # 1) Нет пересечения
        if qr < L or R < ql:
            return 0
        # 2) Полное покрытие
        if ql <= L and R <= qr:
            return tree[node]
        # 3) Частичное — идём в двух детей
        mid = (L + R) // 2
        left_max  = query(node*2,     L,   mid, ql, qr)
        right_max = query(node*2 + 1, mid+1, R,  ql, qr)
        return max(left_max, right_max)
    
    # 6) рекурсивная замена элемента
    def update(idx, val):
        pos = s + idx   # позиция листа
        tree[pos] = val
        pos //= 2
        while pos:
            tree[pos] = max(tree[2*pos], tree[2*pos+1])
            pos //= 2

    out = []
    # 7) отвечаем на запросы
    for _ in range(k):
        type, l, r = input().split()
        if type == 's':
            idx = query(1, 0, s-1, int(l)-1,  int(r)-1)
            out.append(str(idx))
        elif type == 'u':
            update(int(l) - 1, int(r))
    print(" ".join(out))

max_with_update()
