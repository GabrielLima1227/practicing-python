class Song:
    def __init__(self, name, author) -> None:
        self.name = name
        self.author = author

class Playlist:
    def __init__(self, name, songs: list[Song] = None) -> None:
        self.name = name
        self.songs = [] if songs is None else songs

    def add_song(self, song: Song) -> None:
        self.songs.append(song)
        print(f"The song {song.name} has been added to the Playlist")

    def list_of_songs(self) -> None:
        if not self.songs:  
            print("Playlist is empty ")
            return
        for index, song in enumerate(self.songs):
            print(f"{index + 1}. {song.name} - {song.author}")

    def remove_song_from_the_playlist(self, song: Song) -> bool:
        if not self.songs:
            print("Playlist is empty")
            return False
        if song in self.songs:
            self.songs.remove(song)
            return True
        else: 
            return False

my_playlist = Playlist("Rock")

my_song1 = Song("Imagine", "John Lennon")
my_song2 = Song("Bohemian Rhapsody", "Queen")
my_song3 = Song("Stairway to Heaven", "Led Zeppelin")

my_playlist.add_song(my_song1)
my_playlist.add_song(my_song2)


my_playlist.list_of_songs()

print(my_playlist.remove_song_from_the_playlist(my_song1))
print(my_playlist.remove_song_from_the_playlist(my_song3))

print("-=" * 20)

my_playlist.list_of_songs()