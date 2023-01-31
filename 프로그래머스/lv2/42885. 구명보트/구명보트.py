from collections import deque

def solution(people, limit):
    people.sort()
    people=deque(people)
    answer = 0
    big = people.pop()
    small = people.popleft()
    while True:
        if big + small <= limit:
            if len(people) == 0:
                answer += 1
                break
            if len(people) == 1:
                answer += 2
                break
            big = people.pop()
            small = people.popleft()
        else:
            if len(people) == 0:
                answer += 2
                break
            big = people.pop()
        answer += 1

    return answer