from collections import defaultdict

def pretty_string():
    k = int(input().strip())
    letters = input()
    l = 0
    result = 0
    popular = defaultdict(int)
    # Проходим правым указателем по всей строке
    for r in range(len(letters)):
        # либо если не использовать deafaultdict, для обычного dict подойдет
        # popular[letters[r]] = popular.get(letters[r], 0) + 1
        popular[letters[r]] += 1
        most_popular = max(popular.values())
        # Если нужно заменить больше чем k символов, сдвигаем левую границу
        if (r - l + 1) - most_popular > k:
            popular[letters[l]] -= 1
            l += 1
        result = max(result, r - l + 1)
    return result



pretty_string()