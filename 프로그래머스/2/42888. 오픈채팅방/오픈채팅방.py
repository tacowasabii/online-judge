def solution(record):
    answer = []
    
    nick = {}
    
    for i in record:
        if not i.startswith("Leave"):
            a, b, c = i.split(" ")
            nick[b] = c
    for i in record:
        if i.startswith("Enter"):
            a, b, c = i.split(" ")
            answer.append(f"{nick[b]}님이 들어왔습니다.")
        elif i.startswith("Leave"):
            a, b = i.split(" ")
            answer.append(f"{nick[b]}님이 나갔습니다.")
    return answer