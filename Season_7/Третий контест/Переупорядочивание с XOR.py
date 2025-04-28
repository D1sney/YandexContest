# 1) Считываем количество чисел n
n = int(input())

# 2) Считываем числа a1, a2, ..., an
numbers = list(map(int, input().split()))

# 3) Находим максимальное число, чтобы определить длину двоичного представления
max_num = max(numbers)
bit_length = 0
temp = max_num
while temp > 0:
    bit_length += 1
    temp //= 2

# ————————————————
# Способ B: с помощью встроенных Python-функций
bit_length = max(numbers).bit_length()

# 4) Создаём таблицу битов b_bits: каждая строка — число, каждый столбец — позиция бита
b_bits = []
for num in numbers:
    # Берём младший бит bit_length раз, сохраняем, а потом разворачиваем
    binary = []
    for _ in range(bit_length):
        binary.append(num % 2)
        num //= 2
    b_bits.append(binary[::-1])


# 5) Находим все столбцы с нечётным числом единиц
odd_cols = [
    j
    for j in range(bit_length)
    if sum(b_bits[i][j] for i in range(n)) % 2 == 1
]

# Если их количество нечётно — impossible
if len(odd_cols) % 2 == 1:
    print("impossible")
    exit()

# 6) Починка «качелькой» по парам нечётных столбцов
while odd_cols:
    p = odd_cols.pop()
    q = odd_cols.pop()
    for i in range(n):
        # найдена строка, где в p и q разный бит → можем «переставить» единицу
        if b_bits[i][p] != b_bits[i][q]:
            b_bits[i][p], b_bits[i][q] = b_bits[i][q], b_bits[i][p]
            break
    else:
        # если таких строк нет — перестановка невозможна
        print("impossible")
        exit()

# 7) Собираем числа b_i из строк b_bits
# Способ A: вручную через сдвиги
result = []
for row in b_bits:
    x = 0
    for bit in row:
        x = (x << 1) | bit
    result.append(x)

# Вывод (вариант A):
print(*result)

# ————————————————
# Способ B: с помощью встроенных Python-функций
# Собираем каждую строку как строку '01011…' и сразу переводим в int
result2 = [int(''.join(map(str, row)), 2) for row in b_bits]

# Вывод (вариант B):
print(' '.join(map(str, result2)))

