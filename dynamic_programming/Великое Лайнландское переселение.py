
def move_people():
    n = int(input().strip())
    towns = list(map(int, input().split()))
    stack = []
    result = [-1] * n

    for i in range(n):
        while stack and stack[-1][0] > towns[i]:
            _, idx = stack.pop()
            result[idx] = i

        stack.append((towns[i], i))
    print(" ".join(map(str, result)))
    
move_people()
