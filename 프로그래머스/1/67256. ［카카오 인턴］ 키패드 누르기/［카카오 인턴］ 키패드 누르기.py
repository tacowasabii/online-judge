def solution(numbers, hand):
    answer = ''
    dic = {0:(0,0), 1:(-1,3), 2:(0,3), 3:(1,3), 4:(-1,2), 5:(0,2), 6:(1,2), 7:(-1,1), 8:(0,1), 9:(1,1), '*':(-1,0), '#':(1,0)}
    left = '*'
    right = '#'
     
    for i in numbers:
        if i == 3 or i == 6 or i == 9 :
            right = i
            answer += 'R'
        elif i == 1 or i == 4 or i == 7:
            left = i
            answer += 'L'
        else:
            ld = abs(dic[left][0]-dic[i][0]) + abs(dic[left][1]-dic[i][1])
            rd = abs(dic[right][0]-dic[i][0]) + abs(dic[right][1]-dic[i][1])
            if ld > rd or (ld == rd and hand == 'right'):
                right = i
                answer += 'R'
            else:
                left = i
                answer += 'L'
    return answer