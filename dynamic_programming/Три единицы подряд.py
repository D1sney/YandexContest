
def count_sub_rows():
    n = int(input())
    dp = [-1] * (n + 1)

    def f(n):
        if n == 0:
            return 1
        elif n == 1:
            return 2
        elif n == 2:
            return 4
        if dp[n] != -1:
            return dp[n]
        dp[n] = f(n-1) + f(n-2) + f(n-3)
        return dp[n]

    return f(n)

print(count_sub_rows())