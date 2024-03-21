from collections import defaultdict

def solution(tickets):
    answer = []
    
    dic = defaultdict(list)
    for start, arrive in tickets:
        dic[start].append(arrive)
    for i in dic:
        dic[i].sort(reverse = True)
    
    stack = ["ICN"]
    
    while stack:
        tmp = stack[-1]
        
        if tmp in dic and len(dic[tmp]) > 0:
            stack.append(dic[tmp].pop())
        else:
            answer.append(tmp)
            stack.pop()
    
    return answer[::-1]