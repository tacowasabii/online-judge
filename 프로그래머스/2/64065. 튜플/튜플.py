def solution(s):
    s = s[2:-2].split("},{")
    for i in range(len(s)):
        s[i] = set(map(int, s[i].split(",")))
    s.sort(key = lambda x:len(x))
    answer = [list(s[0])[0]]

    for i in range(len(s) - 1):
        answer.append(list(s[i + 1] - s[i])[0])
        
    return answer