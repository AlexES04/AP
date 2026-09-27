def fibonacci_memo(n, memoria=None):
    if memoria is None:
        memoria = {}

    if n <= 1:
        return n

    if n in memoria:
        return memoria[n]

    result = fibonacci_memo(n-1, memoria) + fibonacci_memo(n-2, memoria)

    memoria[n] = result
    return result

def fibonacci_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]