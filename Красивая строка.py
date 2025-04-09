
def pretty_string():
    k = int(input().strip())
    letters = input()
    err = 0
    count = 0
    results = []
    for left in range(len(letters)):
        for right in range(left, len(letters)):
            if right == left:
                count += 1
                continue
            if right != left and err < k:
                err += 1
                count += 1
            else:
                err = 0
                break
        results.append(len(letters[left:right+1]))
    return max(results)

pretty_string()