def solution(s1, s2):
    
    return max(len(s1),len(s2))-max(len(set(s1)-set(s2)),len(set(s2)-set(s1)))