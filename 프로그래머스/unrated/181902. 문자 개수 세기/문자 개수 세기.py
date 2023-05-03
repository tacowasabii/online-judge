def solution(my_string):
    dic = {}
    for i in range(ord('A'), ord('Z') + 1):
        dic[chr(i)] = 0
    for i in range(ord('a'), ord('z') + 1):
        dic[chr(i)] = 0
    for i in my_string:
        dic[i] += 1
    return [v for v in dic.values()]