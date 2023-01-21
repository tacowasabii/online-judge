def solution(babbling):
    answer = 0
    for i in babbling:
        i = i.replace("aya", "1")
        i = i.replace("ye", "1")
        i = i.replace("woo", "1")
        i = i.replace("ma", "1")
        if set(i) == {'1'}:
            answer += 1
    return answer