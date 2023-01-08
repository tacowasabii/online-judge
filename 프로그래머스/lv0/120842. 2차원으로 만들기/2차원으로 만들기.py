def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        a=[]
        for j in range(i*n,(i+1)*n):
            a.append(num_list[j])
        answer.append(a)
    return answer