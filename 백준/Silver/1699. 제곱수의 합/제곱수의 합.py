import sys
import math

def min_square_sum(n):
    if n == 1:
        return 1

    squares = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
    dp = [sys.maxsize] * (n + 1)
    dp[0] = 0

    for square in squares:
        for i in range(square, n + 1):
            dp[i] = min(dp[i], dp[i - square] + 1)

    return dp[n]

print(min_square_sum(int(input())))