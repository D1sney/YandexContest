
def count_max_with_freq():
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
    tree = [(0, 0)] * (2 * s)

    # 3) заполняем листья
    for i in range(n):
        tree[s + i] = (nums[i], 1)
    # от s+n до 2s-1 уже (0,0)

    # 4) combine-функция
    def combine(left, right):
        lv, lc = left
        rv, rc = right
        if lv > rv:
            return (lv, lc)
        elif rv > lv:
            return (rv, rc)
        else:
            return (lv, lc + rc)

    # 5) строим внутренние
    for i in range(s - 1, 0, -1):
        tree[i] = combine(tree[2*i], tree[2*i + 1])

    # 6) рекурсивный запрос
    def query(node, L, R, ql, qr):
        if qr < L or R < ql:
            return (0, 0)
        if ql <= L and R <= qr:
            return tree[node]
        mid = (L + R) // 2
        left_res = query(node*2, L, mid, ql, qr)
        right_res = query(node*2+1, mid+1, R, ql, qr)
        return combine(left_res, right_res)

    out = []
    # 7) отвечаем на запросы
    for _ in range(k):
        l, r = map(int, input().split())
        mx, cnt = query(1, 0, s-1, l-1, r-1)
        out.append(f"{mx} {cnt}")
    print("\n".join(out))

count_max_with_freq()
