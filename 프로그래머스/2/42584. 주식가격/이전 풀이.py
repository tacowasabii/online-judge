def solution(prices):
    answer = []
    dic = {}
    stack = []
    for i, v in enumerate(prices):
        while len(stack) > 0:
            tmp = stack.pop()
            if tmp[1] > v:
                dic[tmp[0]] = i - tmp[0]
            else:
                stack.append(tmp)
                break
        stack.append((i,v))
    if len(stack) > 0:
        for i in stack:
            dic[i[0]] = len(prices) - 1 - i[0]
            
    for i in range(len(prices)):
        answer += [dic[i]]
    return answer

# prices를 순회하면서 stack에 (인덱스, 가격)을 넣는다.
# stack의 top이 현재 가격보다 크면 pop하면서 현재 인덱스와의 차이를 저장한다.
# stack의 top이 현재 가격보다 작거나 같으면 push한다.
# prices를 다 돌고 stack에 남아있는 값들을 pop하면서 차이를 저장한다.
# 저장된 차이들을 answer에 넣어 반환한다.
# 시간 복잡도는 O(n)이다.