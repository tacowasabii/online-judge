def solution(n, lost, reserve):
    # set을 사용하여 중복을 제거
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for r in set_reserve:
        if r-1 in set_lost:
            set_lost.remove(r-1)
        elif r+1 in set_lost:
            set_lost.remove(r+1)
            
    # 전체 학생 수에서 여전히 유니폼이 없는 학생의 수를 빼서 반환
    return n - len(set_lost)
