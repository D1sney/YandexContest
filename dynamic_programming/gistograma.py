def get_gistograma():
    symbols = []
    with open("input.txt", "r", encoding="utf-8") as file:
        for line in file:
            for ch in line:
                if ch.isspace():
                    continue
                symbols.append(ch)
    
    stack = {}
    for i in symbols:
        if not i in stack:
            stack[i] = 1
        else:
            stack[i] += 1
    
    list_stack = sorted(stack)
    for high in range(max(stack.values()), 0, -1):
        for check in list_stack:
            if stack[check] >= high:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(list_stack))
        
get_gistograma()
