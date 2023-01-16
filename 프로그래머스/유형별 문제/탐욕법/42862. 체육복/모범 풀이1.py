# 앞 뒤에 1을 하나씩 넣음
def solution(n, lost, reserve):
    a = [1] * (n + 2)

    for i in lost:
        a[i] -= 1 #O(n)
    for i in reserve:
        a[i] += 1 #O(n)
    for i in range(1,n+1): #O(n)
        if a[i-1] == 0 and a[i] == 2:
            a[i -1:i + 1] = [1, 1]
        if a[i] == 2 and a[i + 1] == 0:
            a[i:i + 1] = [1, 1]
    return len([x for x in a[1:-1] if x>0]) #O(n)

    #O(n)