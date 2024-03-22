def solution(babbling):
    pr = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for i in babbling:
        flag = 1
        tmp = ''
        while len(i) > 0 and flag == 1:
            flag = 0
            for j in pr:
                if j != tmp and i.startswith(j):
                    i = i[len(j):]
                    tmp = j
                    flag = 1
                    continue
            if len(i) == 0:
                cnt += 1
            if flag == 0:
                break
    return cnt