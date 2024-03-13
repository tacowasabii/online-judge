def solution(word):
    answer = 0
    alph = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    
    for i, v in enumerate(word):
         for j in range(5 - i):
                answer += alph[v] * 5 ** j
         answer += 1
    return answer