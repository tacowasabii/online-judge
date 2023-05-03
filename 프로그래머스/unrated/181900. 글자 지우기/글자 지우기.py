def solution(my_string, indices):
    tmp = list(my_string)
    for i in indices:
        tmp[i]=''
    return ''.join(tmp)