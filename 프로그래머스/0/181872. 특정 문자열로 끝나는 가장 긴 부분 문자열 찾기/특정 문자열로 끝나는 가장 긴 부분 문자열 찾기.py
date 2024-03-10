def solution(myString, pat):
    idx = myString[::-1].find(pat[::-1])
    return myString[:len(myString)-idx]