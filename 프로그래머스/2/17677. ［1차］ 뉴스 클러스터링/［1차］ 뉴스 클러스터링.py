def isAlph(str):
    if ord('a') <= ord(str) <= ord('z'):
        return True

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = []
    s2 = []
    for i in range(len(str1)-1):
        if isAlph(str1[i]) and isAlph(str1[i+1]):
            s1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if isAlph(str2[i]) and isAlph(str2[i+1]):
            s2.append(str2[i:i+2])      
    
    if len(s1) == 0 and len(s2) == 0:
        return 65536
    intersection = 0
    
    for i in list(set(s1)):
        if i in s2:
            intersection += min(s1.count(i), s2.count(i))
            
    union = 0
    for i in list(set(s1)):
        if i in s2:
            union += max(s1.count(i), s2.count(i))
        else:
            union += s1.count(i)
    for i in list(set(s2)):
        if i not in s1:
            union += s2.count(i)
    return int((intersection / union) * 65536)