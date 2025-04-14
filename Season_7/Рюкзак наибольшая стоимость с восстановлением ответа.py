
def back_pack():
    n, bp_max = map(int, input().split())
    kilo = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    bp = [[-1] * n for _ in range(bp_max + 1)]
    for i in bp:
        i[0] = 0

    for i in range(n):
        for j in range(bp_max - kilo[i], -1, -1):
            if bp[j][i] == -1:
                continue
            else:
                if j + kilo[i] <= bp_max:
                    bp[j + kilo[i]][i] = (max(bp[j + kilo[i]][i], bp[j][i] + cost[i]), i+1)
                    # пока что записал только стоимость в нужную клетку по высоте, но еще надо записать предыдущий предмет
    
    res = 0

    # Находим лучшую стоимость по последнему столбцу (без изменения порядка строк)
    most_thing = max((m[-1] for m in bp), key=lambda m: m[0])
    res = most_thing[0]

    # определили вес текущего предмета
    current_weight = None
    for w in range(bp_max + 1):
        cell = bp[w][-1]
        if cell[0] == res:
            current_weight = w
            break
    
    # Начинаем с последнего столбца, поскольку мы искали результат в bp[*][-1]
    current_row = n - 1
    story = []

    while current_weight > 0 and current_row >= 0:
        cell = bp[current_weight][current_row]
        last_item = cell[1]
        if last_item > 0:  # Проверяем, что предмет реальный
            story.append(last_item)
            current_weight -= kilo[last_item - 1]
            current_row = last_item - 1  # Переходим к предметам до last_item
        else:
            current_row -= 1  # Если предмет не взят, проверяем предыдущий

    # Полученная последовательность восстановлена в обратном порядке, раз перевели от последнего добавленного
    story.reverse()
    for item in story:
        print(item)

back_pack()