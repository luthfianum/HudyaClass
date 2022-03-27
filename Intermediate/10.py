songs = [
    {"artist": "Taylor Swift", "song": "Firework"},
    {"artist": "Justin Bieber", "song": "Intentions"},
]

def find_song(song):
    song = song.lower()
    
    for item in songs:
        if item['song'].lower() == song:
            return playlist.append(item)
    return f"No song found: {song}"


playlist = []

while True:
    song = input("Masukkan judul lagu: ")
    
    if song == "done":
        break
    find_song(song)
    
print(playlist)