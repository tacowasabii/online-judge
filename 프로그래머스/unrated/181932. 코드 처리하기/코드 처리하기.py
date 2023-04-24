def solution(code):
    answer = ''
    mode=True
    for i in range(len(code)):
        if code[i]=='1':
            mode= not mode
        else:
            if (i%2==0 and mode) or (i%2!=0 and not mode):
                answer+=code[i]
    if answer=='':
        return 'EMPTY'          
        
    return answer