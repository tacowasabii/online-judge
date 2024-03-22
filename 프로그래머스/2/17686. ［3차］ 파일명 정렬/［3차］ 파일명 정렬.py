def split_filename(filename):
    h, n = '', ''
    index = 0

    for i in filename:
        if i.isdecimal():
            break
        h += i
        index += 1
    
    for i in range(index, index + 5):
        if i >= len(filename) or not filename[i].isdecimal():
            break
        n += filename[i]
    
    return h, n
    
def solution(files):
    def file_sort_key(filename):
        h, n = split_filename(filename)
        
        return [h.lower(), int(n)]

    return sorted(files, key = file_sort_key)