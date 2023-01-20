def solution(id_pw, db):
    flag = 0
    for i in db:
        if i[0] == id_pw[0]:
            if i[1] != id_pw[1]:
                flag = 1
            else:
                return "login"
    if flag == 1:
        return "wrong pw"
    elif flag == 0:
        return "fail"
