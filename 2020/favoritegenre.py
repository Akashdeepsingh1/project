

def genre(userSongs, songGenres):
    genre_song = {}
    for k, v in songGenres.items():
        for each in v:
            genre_song[each] = k

    userGenre = {}
    final_list = {}
    for k,v in userSongs.items():
        temp = {}
        temp_max = 0
        temp_list = []
        for each in v:
            if genre_song[each] in temp:
                temp[genre_song[each]] +=1
                if temp_max == temp[genre_song[each]]:
                    temp_list.append(genre_song[each])
                elif temp_max<temp[genre_song[each]]:
                    temp_list = [genre_song[each]]
                    temp_max = temp[genre_song[each]]
            else:
                temp[genre_song[each]] = 1
                if temp_max ==0 or temp_max == 1:
                    temp_list.append(genre_song[each])
                    if temp_max == 0:
                        temp_max+=1

        userGenre[k] = temp
        final_list[k] = temp_list

    for k,v in final_list.items():
        print('{}  {}'.format(k,v))


def favGenres (userSongs, songGenres):
    output = {}
    for user in userSongs:
        song_list = userSongs[user]
        count = {}

        for song in song_list:
            for genre in songGenres:
                if (song in songGenres[genre]):
                    count[genre] = count.get (genre, 0) + 1

        output[user] = [key for key, val in count.items () if val == max (count.values ())]

    return output




userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}


genre(userSongs,songGenres)
favGenres(userSongs,songGenres)