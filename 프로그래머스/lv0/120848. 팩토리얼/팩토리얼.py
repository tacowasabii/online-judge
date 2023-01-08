def solution(n):
    a=1
    b=1
    while(a<=n):
        a*=b
        b+=1
    return b-2