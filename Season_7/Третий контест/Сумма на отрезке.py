
def sum_on_segment():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())

    # 1) размер под дерево (минимальная степень двойки ≥ n)
    s = 1
    while s < n:
        s <<= 1

    # 2) массив-дерево, изначально нули
    tree = [0] * (2 * s)

    # 5) рекурсивный запрос суммы на отрезке [ql, qr]
    def query(node, L, R, ql, qr):
        if qr < L or R < ql:
            return 0
        if ql <= L and R <= qr:
            return tree[node]
        mid = (L + R) // 2
        return query(node*2,     L,   mid, ql, qr) + \
               query(node*2 + 1, mid+1, R,  ql, qr)

    # 6) рекурсивная замена элемента — присвоить a[idx] = val
    def update(idx, val):
        pos = s + idx
        tree[pos] = val
        pos //= 2
        while pos:
            tree[pos] = tree[2*pos] + tree[2*pos+1]
            pos //= 2

    out = []
    # 7) отвечаем на запросы
    for _ in range(k):
        parts = input().split()
        typ = parts[0]
        l = int(parts[1])
        r = int(parts[2])
        if typ == 'Q':
            # запрос суммы [l-1, r-1]
            res = query(1, 0, s-1, l-1, r-1)
            out.append(str(res))
        else:  # 'A'
            # присвоить a[l-1] = r
            update(l-1, r)

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    sum_on_segment()
