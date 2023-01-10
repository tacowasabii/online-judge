def solution(my_str, n):
    answer = []
    a = len(my_str)
    for i in range(a//n):
        answer.append((my_str[i*n:i*n+n]))
    if a%n!=0:
        answer.append(my_str[(a//n)*n:])
    return answer