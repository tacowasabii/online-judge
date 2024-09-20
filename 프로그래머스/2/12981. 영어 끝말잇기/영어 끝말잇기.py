def solution(n, words):
    record = [words[0]]
    for i in range(1, len(words)):
        if words[i] not in record and record[-1][-1] == words[i][0]:
            record.append(words[i])
        else:
            return [i % n + 1, i // n + 1]
    return [0, 0]
