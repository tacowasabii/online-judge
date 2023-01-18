def solution(numlist, n):
    answer = []
    numlist.append(n)
    numlist.sort()
    a = numlist.index(n)
    numlist.remove(n)
    smaller = numlist[:a]
    smaller.sort(reverse=True)
    bigger = numlist[a:]
    while len(smaller) != 0 or len(bigger) != 0:
        if len(smaller) == 0:
            answer.append(bigger[0])
            bigger.pop(0)
        elif len(bigger) == 0:
            answer.append(smaller[0])
            smaller.pop(0)
        elif abs(n - smaller[0]) > abs(n - bigger[0]):
            answer.append(bigger[0])
            bigger.pop(0)
        elif abs(n - smaller[0]) < abs(n - bigger[0]):
            answer.append(smaller[0])
            smaller.pop(0)
        else:
            answer.append(bigger[0])
            answer.append(smaller[0])
            bigger.pop(0)
            smaller.pop(0)
    return answer