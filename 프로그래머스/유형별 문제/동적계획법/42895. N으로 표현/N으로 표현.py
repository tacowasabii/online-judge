def solution(N, number):
    answer = 1
    a = [[], [N]]
    while answer <= 8:
        if number in a[answer]:
            return answer
        answer += 1
        temp = []
        temp.append(int(str(N) * answer))
        for i in range(1, len(a)):
            for j in a[i]:
                for k in a[len(a) - i]:
                    temp.append(j + k)
                    temp.append(j - k)
                    temp.append(j * k)
                    if k != 0:
                        temp.append(j // k)
        a.append(list(set(temp)))

    return -1