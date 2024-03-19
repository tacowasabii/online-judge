from collections import deque

def solution(people, limit):
    people.sort(reverse = True)
    people = deque(people)
    ans = 0
    while people:
        tmp = people.popleft()
        if people and tmp + people[-1] <= limit:
            people.pop()
        ans += 1

    return ans