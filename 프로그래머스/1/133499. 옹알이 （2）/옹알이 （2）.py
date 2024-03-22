def solution(babbling):
    prs = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for i in babbling:
        tmp = ''
        while i:
            length = len(i)
            for pr in prs:
                if i.startswith(pr) and pr != tmp:
                    tmp = pr
                    i = i[len(pr):]
            if length == len(i):
                break
        if not i:
            cnt += 1
    return cnt