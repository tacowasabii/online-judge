def solution(denum1, num1, denum2, num2):
    a= denum1*num2 + denum2*num1
    b= num1*num2
    c=1
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            c=i
            break
    answer = []
    answer.append(a/c)
    answer.append(b/c)
    return answer