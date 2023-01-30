def solution(n, words):
    idx = -1
    used = [words[0]]
    for i in range(len(words) - 1):
        if words[i][-1] != words[i + 1][0] or words[i + 1] in used:
            idx = i + 2
            break
        used.append(words[i + 1])
    if idx == -1:
        return [0, 0]

    return [idx % n if idx % n != 0 else n, idx // n if idx % n == 0 else idx // n + 1]
