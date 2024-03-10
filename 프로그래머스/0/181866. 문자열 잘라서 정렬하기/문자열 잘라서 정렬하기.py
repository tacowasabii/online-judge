def solution(myString):
    filtered_list = [s for s in myString.split('x') if s]
    return sorted(filtered_list)