def solution(a, b, c, d):
    tmp = [a, b, c, d]
    if len(set(tmp)) == 1:
        return a * 1111
    elif len(set(tmp)) == 4:
        return min(tmp)
    elif len(set(tmp)) == 3:
        for i in tmp:
            if tmp.count(i) == 2:
                tmp.remove(i)
                tmp.remove(i)
                return tmp[0] * tmp[-1]
    else:
        for i in set(tmp):
            if tmp.count(i) == 2:
                p = list(set(tmp))[0]
                q = list(set(tmp))[1]
                return (p + q) * abs(p - q)
            elif tmp.count(i) == 3:
                tmp.remove(i)
                tmp.remove(i)
                tmp.remove(i)
                return (10 * i + tmp[0]) ** 2