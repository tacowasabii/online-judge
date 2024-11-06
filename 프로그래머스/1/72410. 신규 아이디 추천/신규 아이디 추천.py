def solution(new_id):
    new_id = new_id.lower()
    tmp = []
    for i in new_id:
        if ord('a') <= ord(i) <= ord('z') or i.isdigit() or i =='-' or i =='_' or i=='.':
            tmp.append(i)
    for i in range(len(tmp) - 1):
        if tmp[i] == '.' and tmp[i+1] == '.':
            tmp[i] = ''
    tmp = ''.join(tmp)
    tmp = tmp.strip('.') 
    if not tmp:
        tmp += 'a'
    new_id = tmp[:15]
    new_id = new_id.rstrip('.')
    
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id