def solution(storey):
    if storey <= 5:
        return storey
    q, r = divmod(storey, 10)
    return min(solution(q) + r, solution(q+1) + (10-r))