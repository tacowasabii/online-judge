def solution(rank, attendance):
    tmp = []
    for i in range(len(rank)):
        if attendance[i]:
            tmp.append(rank[i])
    tmp.sort()
    return 10000*rank.index(tmp[0]) + 100*rank.index(tmp[1]) + rank.index(tmp[2])