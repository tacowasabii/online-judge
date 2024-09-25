def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    set1 = set()
    set2 = set()
    dict1 = {}
    dict2 = {}
    
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            set1.add(str1[i:i + 2])
            dict1[str1[i:i + 2]] = dict1.get(str1[i:i + 2], 0) + 1
            
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            set2.add(str2[i:i + 2])
            dict2[str2[i:i + 2]] = dict2.get(str2[i:i + 2], 0) + 1
    
    if len(set1) == 0 and len(set2) == 0:
        return 65536
    
    union = set1 | set2
    intersection = set1 & set2
    
    cnt1 = 0
    cnt2 = 0
    
    for i in intersection:
        cnt1 += min(dict1[i], dict2[i])
    for i in union:
        cnt2 += max(dict1.get(i, 0), dict2.get(i, 0))
    
    return int(cnt1 / cnt2 * 65536)