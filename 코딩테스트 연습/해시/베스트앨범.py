def solution(genres, plays):
    genre_plays = {}
    answer = []
    for genre, play, index in zip(genres, plays, range(len(genres))):
        if genre not in genre_plays.keys(): genre_plays[genre] = [[(play, index)], play]
        else:
            genre_plays[genre][0].append((play, index))
            genre_plays[genre][1] += play
    for item in sorted(genre_plays.items(), key=lambda x: x[-1][-1], reverse=True):
        for _, index in sorted(item[-1][0], key=lambda x:x[0], reverse=True)[:2]: answer.append(index)

    return answer

if __name__ == '__main__':
    genres = ['classic', 'pop', 'classic', 'classic', 'pop']
    plays = [500, 600, 150, 800, 2500]

    print(solution(genres, plays))