def solution(genres, plays):
    answer = []
    dic = {}
    
    for i, v in enumerate(genres):
        dic[v] = dic.get(v, 0) + plays[i]

    genre_play = list(dic.items())
    genre_play.sort(key = lambda x:x[1], reverse=True)
    sorted_genres = [i[0] for i in genre_play]

    songs = [[] for _ in range(len(sorted_genres))]
    
    for i, v in enumerate(genres):
        songs[sorted_genres.index(v)].append((plays[i], i))
    for i in songs:
        i.sort(key = lambda x:x[0], reverse= True)
        answer.append(i[0][1])
        if len(i) > 1:
            answer.append(i[1][1])
        
    return answer