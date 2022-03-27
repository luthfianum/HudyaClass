playlist = [
    {"artist": "Taylor Swift", "song": "Firework"},
    {"artist": "Justin Bieber", "song": "Intentions"},
]

def find_playlist(artist, song):
    artist = artist.lower()
    song = song.lower()
    for item in playlist:
        if item['artist'].lower() == artist and item['song'].lower() == song:
            return f"We found artist: {artist} and song: {song} in our playlist"
        
    return "We can't found artist: {} and song: {} in our playlist".format(artist, song) 

artist = "Justin Bieber"
song = "firework"
music_1 = find_playlist(artist, song)
print(music_1)

artist = "taylor swift"
song = "firework"
music_2 = find_playlist(artist, song)
print(music_2)

artist = "justin biEber"
song = "IntEntions"
music_3 = find_playlist(artist, song)
print(music_3)