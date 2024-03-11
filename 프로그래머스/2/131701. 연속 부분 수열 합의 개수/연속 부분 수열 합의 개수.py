def solution(elements):
    answer = set()
    tmp = elements + elements
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.add(sum(tmp[j:j+i+1]))
    return len(answer)