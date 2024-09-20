from collections import deque

def solution(people, limit):
    ans = 0
    people.sort()
    people = deque(people)
    while people:
        weight = 0
        weight += people.pop()
        if people and people[0] + weight <= limit:
            people.popleft()
        ans += 1
    return ans