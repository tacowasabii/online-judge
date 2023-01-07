def solution(numbers):
    answer = 0
    for i,a in enumerate(numbers):
        answer+=a
    return answer/(i+1)