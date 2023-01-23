def solution(s):
    zerosum = 0
    count = 0
    while True:
        zerosum += s.count("0")
        s = s.replace("0", "")
        count += 1
        if s == "1":
            break
        s = format(len(s), 'b')
        
    return [count, zerosum]