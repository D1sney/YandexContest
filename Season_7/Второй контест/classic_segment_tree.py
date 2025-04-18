
def count_max():
    # количество чисел в массиве
    n = int(input())
    # элементы массива
    nums = list(map(int, input().split()))
    # количество запросов на вычисление максимума
    k = int(input())
    tree = []
    # ищем минимальную степень двойки которая больше n
    s = 1
    while s < n:
        s *= 2

    tree = [0] * (2 * s)

    # nums[i] на позиции tree[s+i]
    for i in range(n):
        tree[s + i] = nums[i]
    # подложим нули (нейтральный для max)
    for i in range(n, s):
        tree[s + i] = 0
    # cтроим внутренние узлы (от s−1 до 1)
    for i in range(s - 1, 0, -1):
        tree[i] = max(tree[2*i], tree[2*i + 1])

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

    for _ in range(k):
        l, r = map(int, input().split())
        m = query(1, 0, n-1, l-1, r-1)
        print(m)

count_max()