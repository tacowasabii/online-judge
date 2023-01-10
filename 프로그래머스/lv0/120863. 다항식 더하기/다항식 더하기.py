def solution(polynomial):
    answer = ''
    a =polynomial.split(" + ")
    b=[]
    n=0
    c=0
    for i in a:
        if i.isdecimal():
            n+=int(i)
        else:
            b.append(i)
    for j in b:
        if j=='x':
            c+=1
        else:
            c+=int(j[:-1])
    if n==0:
        if c==1:
            return "x"
        return str(c)+"x"
    else:
        if c==0:
            return str(n)
        else:
            if c==1:
                return "x"+" + "+str(n)
            return str(c)+"x"+" + "+str(n)