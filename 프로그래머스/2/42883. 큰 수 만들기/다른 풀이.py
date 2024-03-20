def solution(number, k):
    collected = []
    for i, num in enumerate(number):  # O(n)
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        # k가 0이면 나머지 숫자들을 모두 추가
        # 바로 break 시키면서 효율성을 조금 높일 수 있음
        if k == 0:
            collected += list(number)[i:]
            break
        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    
    return answer

# O(n)