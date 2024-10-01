def solution(babbling):
    prs = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for word in babbling:
        prev_pr = ""
        i = 0
        while i < len(word):
            found = False
            for pr in prs:
                if word[i:].startswith(pr) and prev_pr != pr:
                    prev_pr = pr
                    i += len(pr)
                    found = True
            if not found:
                break
        if i == len(word):
            cnt += 1
            
    return cnt
            