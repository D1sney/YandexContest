
def k_null():
    import sys
    input = sys.stdin.readline

    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())

    # 1) размер под дерево
    s = 1
    while s < n:
        s *= 2

    # 2) дерево
    NEUTRAL = ((10**18), 0)
    tree = [NEUTRAL] * (2 * s)

    # 3) заполняем листья, кладем индекс i + 1
    for i in range(n):
        tree[s + i] = (nums[i], i+1)
    # от s+n до 2s-1 уже NEUTRAL

    # 4) combine
    def combine(left, right):
        return right if right[0] < left[0] else left

    # 5) строим внутренние
    for i in range(s - 1, 0, -1):
        tree[i] = combine(tree[2*i], tree[2*i + 1])

    # 6) рекурсивный запрос
    def query(node, L, R, ql, qr):
        if qr < L or R < ql:
            return NEUTRAL
        if ql <= L and R <= qr:
            return tree[node]
        mid = (L + R) // 2
        left_res = query(node*2, L, mid, ql, qr)
        right_res = query(node*2+1, mid+1, R, ql, qr)
        return combine(left_res, right_res)
    
    # 7) рекурсивная замена элемента
    def update(idx, val):
        pos = s + idx   # позиция листа
        tree[pos] = val
        pos //= 2
        while pos:
            tree[pos] = max(tree[2*pos], tree[2*pos+1])
            pos //= 2

    out = []
    # 8) отвечаем на запросы
    for _ in range(k):
        type, l, r = input().split()
        if type == 's':
            num, idx = query(1, 0, s-1, int(l)-1,  int(r)-1)
            if num != 0:
                out.append(str(-1))
            else:
                out.append(str(idx + 1))
        elif type == 'u':
            update(int(l) - 1, int(r))
    print(" ".join(out))

k_null()