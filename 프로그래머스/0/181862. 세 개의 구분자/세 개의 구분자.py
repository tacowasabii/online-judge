def solution(myStr):
    answer = []
    tb = str.maketrans("abc","   ")
    new_str = myStr.translate(tb)
    return new_str.split() if len(new_str.split())!=0 else ["EMPTY"]