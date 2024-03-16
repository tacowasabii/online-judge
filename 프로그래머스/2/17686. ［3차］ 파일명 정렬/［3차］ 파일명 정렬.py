import re

def split_filename(filename):
    h, n = '', ''
    index = 0
    
    while not filename[index].isdigit():
        h += filename[index]
        index += 1
    
    cnt = 0
    while index < len(filename) and cnt < 5:
        if not filename[index].isdigit():
            break
        n += filename[index]
        index += 1
        cnt += 1
    
    return h, n

def solution(files):
    def file_sort_key(filename):
        head, number = split_filename(filename)
        return [head.lower(), int(number)]

    return sorted(files, key = file_sort_key)