def solution(wallet, bill):
    answer = 0
    wallet.sort()
    bill.sort()
    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        bill[1] //= 2
        answer += 1
        bill.sort()
    return answer