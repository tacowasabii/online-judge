def solution(s):
    answer = []
    a = s.strip("{}").split('},{')
    tmp = []
    for i in a:
        tmp.append(i.split(','))
    tmp.sort(key = lambda x:len(x))
    sets = set()
    for i in tmp:
        answer.append(int(list(set(i) - sets)[0]))
        sets = set(i)
    return answer