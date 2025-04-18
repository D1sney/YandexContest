
def back_pack():
    n, bp_max = map(int, input().split())
    kilo = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    bp = (bp_max + 1) * [-1]
    bp[0] = 0
    for i in range(len(kilo)):
        for j in range(bp_max - kilo[i], -1, -1):
            if bp[j] == -1:
                continue
            else:
                if j + kilo[i] <= bp_max:
                    bp[j + kilo[i]] = max(bp[j + kilo[i]], bp[j] + cost[i])
    return max(bp)

print(back_pack())