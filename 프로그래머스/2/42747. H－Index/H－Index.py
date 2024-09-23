def solution(citations):
    citations.sort()
    for i, v in enumerate(citations):
        if len(citations) - i <= v:
            return len(citations) - i
    return 0