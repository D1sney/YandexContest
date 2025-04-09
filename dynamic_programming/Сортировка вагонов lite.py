
def sort_train():
    n = int(input().strip())
    wagons = list(map(int, input().split()))
    stack = []
    expected = 1

    for wagon in wagons:
        stack.append(wagon)
        # Если верхний вагон в стеке соответствует ожидаемому, выводим его на путь 2, мы можем вывести сразу несколько вагонов, если они выстроены в правильном порядке
        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1

    if expected == n + 1:
        print("YES")
    else:
        print("NO")

sort_train()