def solution(m, n, puddles):
    table = [[0] * m for _ in range(n)]
    table[0][0] = 1
    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] not in puddles:
                if 0 < j and [j,i + 1] not in puddles:
                    table[i][j] += table[i][j - 1]
                if 0 < i and [j + 1,i] not in puddles:
                    table[i][j] += table[i - 1][j]
                    
    return table[n -1][m - 1] % 1000000007