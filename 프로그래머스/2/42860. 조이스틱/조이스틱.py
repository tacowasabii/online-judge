def solution(name):
    # 총 조작 횟수를 저장할 변수 초기화
    answer = 0
    # 이름의 길이
    n = len(name)
    # 최소 좌우 이동 횟수의 초기값 설정: 맨 왼쪽에서 시작하여 오른쪽 끝으로 이동하는 경우
    min_move = n - 1

    for i, char in enumerate(name):
        # 각 알파벳을 변경하는데 필요한 최소 횟수를 더함 (A에서 시작하여 위로 가는 횟수와 아래로 가는 횟수 중 작은 값)
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 현재 문자 다음으로, 'A'가 아닌 다음 문자를 찾음
        next = i + 1
        # 연속된 'A'를 건너뛰는 동안 next를 증가시킴
        while next < n and name[next] == 'A':
            next += 1

        # i: 현재 위치까지 오고 다시 돌아가는 이동 횟수
        # n - next: 마지막 'A'가 아닌 문자로부터 끝까지의 거리
        # min(i, n - next): 현재 위치에서 뒤로 돌아가는 것과 계속 전진하는 것 중 더 짧은 이동 거리 선택
        distance = min(i, n - next)
        # 현재까지의 최소 이동과, 새로 계산한 이동 거리를 비교하여 더 작은 값으로 min_move 갱신
        min_move = min(min_move, i + n - next + distance)

    # 총 조작 횟수(알파벳 변경 + 최소 이동 횟수) 반환
    answer += min_move
    return answer
