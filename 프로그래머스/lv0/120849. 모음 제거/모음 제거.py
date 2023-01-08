def solution(my_string):
    a=['a','i','o','u','e']
    answer = ''
    for i in my_string:
        if not i in a:
            answer+=i
    return answer