def solution(quiz):
    answer = []
    for i in quiz:
        a=i.split()
        if a[1]=='+':
            answer.append('O') if (int(a[0])+int(a[2])) == int(a[4]) else answer.append('X')
        else:
            answer.append('O') if (int(a[0])-int(a[2])) == int(a[4]) else answer.append('X')
    return answer