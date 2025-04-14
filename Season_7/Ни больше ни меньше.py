
def not_more_not_less():
    cycle = int(input())
    for _ in range(cycle):
        n = int(input())
        nums = list(map(int, input().split()))
        
        now = []
        current_min = 0  # переменная для текущего минимума в отрезке
        result = []
        count = 0
        
        for num in nums:
            if not now:
                # Если отрезок пустой, добавляем элемент и устанавливаем current_min
                now.append(num)
                current_min = num
            else:
                new_min = current_min if current_min < num else num  # аналог: new_min = min(current_min, num)
                # Проверка: если при добавлении нового элемента 
                # новый минимум отрезка new_min >= (длина текущего отрезка + 1)
                if new_min >= len(now) + 1:
                    now.append(num)
                    current_min = new_min  # обновляем минимум в отрезке
                else:
                    result.append(len(now))
                    count += 1
                    # Начинаем новый отрезок, включив текущий элемент, и сбрасываем current_min
                    now = [num]
                    current_min = num
                        
        if now:
            result.append(len(now))
            count += 1
        
        print(count)
        print(*result)

not_more_not_less()