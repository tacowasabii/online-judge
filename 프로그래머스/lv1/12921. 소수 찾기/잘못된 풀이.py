def solution(n):
    num = [x for x in range(2, n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        for j in num:
            if j != i and j % i == 0:
                num.remove(j)
    return len(num)
  
# 시간 초과
