
def back_pack():
    n, bp_max = map(int, input().split())
    kilo = list(map(int, input().split()))

    bp = [-1] * (bp_max + 1)
    bp[0] = 0
    for i in kilo:
        for j in range(bp_max - i, -1, -1):
            if bp[j] == -1:
                continue
            else:
                if bp[j] + i < bp_max:
                    bp[j + i] = j
    return [weight for weight in range(bp_max, -1, -1) if bp[weight] != -1][0]

print(back_pack())