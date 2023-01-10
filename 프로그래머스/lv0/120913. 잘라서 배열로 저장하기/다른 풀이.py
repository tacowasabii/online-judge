def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]
    
# 인덱스 슬라이싱에서 마지막은 인덱스를 벗어나도 상관없음
