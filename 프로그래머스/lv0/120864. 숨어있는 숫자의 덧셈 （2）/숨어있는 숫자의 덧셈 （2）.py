def solution(my_string):
    a=my_string
    for i in my_string:
        if ord(i)>=65 and ord(i)<=122:
            my_string=my_string.replace(i,'+')
    if my_string[-1]=='+':
        my_string+='0'
    return eval(my_string)