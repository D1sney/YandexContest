# Читаем входные данные
N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

# Вычисляем массив a
a = []
for i in range(N):
    # Берем побитовое ИЛИ всех m[i][j] для j != i
    result = 0
    for j in range(N):
        if i != j:  # Пропускаем диагональ (m[i][i] = 0)
            result |= m[i][j]  # Побитовое ИЛИ в Python — |=
    a.append(result)

# Проверяем решение (для отладки, можно убрать)
for i in range(N):
    for j in range(N):
        if i != j:
            if (a[i] & a[j]) != m[i][j]:  # Проверяем, что a[i] & a[j] = m[i][j]
                print(f"Ошибка в m[{i}][{j}]")

# Выводим результат
print(*a)