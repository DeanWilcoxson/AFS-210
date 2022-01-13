from playsound import playsound
class NewDoubleEndedQueue():
    def __init__(self):
        self.items = []

    def __iter__(self):
        for x in self.items:
            yield x

    def clear(self):
        self.items.clear()

    def count(self, item):
        self.count(item)

    def index(self, item):
        self.items.index(item)

    def append(self, item):
        self.items.append(item)

    def appendLeft(self, item):
        self.items.insert(0, item)

    def insertAtIndex(self, index, item):
        self.items.insert(index, item)

    def pop(self):
        self.items.pop()

    def popLeft(self):
        self.items.pop(0)

    def removeAtIndex(self, index):
        self.items.pop(index)

    def reverse(self):
        self.items.reverse()

    def rotate(self):
        self.items = self.items[len(self.items)//3:] + \
            self.items[:len(self.items)//3]
        return self.items

    def sort(self):
        self.items.sort()
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def __str__(self):
        return self.title + " by " + self.artist

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
class mediaPlayer():
    def __init__(self):
        self.playlist = NewDoubleEndedQueue()
    """self.playlist is pointing to the deque as its abstract data structure (Built upon a list)"""

    def addSong(self):
        # Add code to prompt user for Song Title and Artist Name
        songName = input("Song Title: ")
        songArtist = input("Artist Name: ")
        song = Song(songName, songArtist)
        # Add song to playlist
        self.playlist.append(song)
        print("Song Added to Playlist")
    """The addSong function creates a song object with the values of the users inputs. It sends them through the Song class and appends the returned object to the playlist"""

    def removeSong(self):
        if len(self.playlist.items):
            count = 0
            # display songs with index position in front
            for i in self.playlist:
                print(count, ":", i)
                count += 1
            # Prompt user for Song Index
            index = int(input("Remove which track: "))
            # remove song from playlist
            self.playlist.removeAtIndex(index)
            print("Song Removed from Playlist")
        else:
            print("There are no songs in your playlist yet.")
    """The removeSong function loops through and displays the playlist and a user input decides which index is removed"""

    def playSong(self):
        # Play the playlist from the beginning
        print("Playing....")
        playsound("C:\\Users\\Gainious\\Dev\\media_files\\Guile's Theme.mp3")
        # Display song name that is currently playing
        return
    """"""

    def skipSong(self):
        # Skip to the next song on the playlist
        print("Skipping....")
        # Display song name that is now playing
        pass
    """"""

    def prevSong(self):
        # Go back to the previous song on the playlist
        print("Replaying....")
        # Display song name that is now playing
        pass
    """"""

    def shuffle(self):
        if len(self.playlist.items):
            print("Shuffling....")
            self.playlist.rotate()
            self.displayPlaylist()
        else:
            print("There are no songs in your playlist yet.")
    """The Shuffle Function calls the rotate method of the deque class which splices the list by three on both sides and swapping the values."""

    def sortPlaylist(self):
        # Sort playlist by Title(alphabetically)
        if len(self.playlist.items):
            print("Sorting by title....")
            self.playlist.sort()
            self.displayPlaylist()
        else:
            print("There are no songs in your playlist yet.")
    """The Sort Playlist Function uses the built in sort method for lists"""

    def currentlyPlaying(self):
        # Display the song name and artist of the currently playing song
        if len(self.playlist.items):
            for i in self.playlist:
                print("Currently playing: ", i, end="")
        else:
            print("There are no songs in your playlist yet.")
    """"""

    def displayPlaylist(self):
        if len(self.playlist.items):
            # Show the current song list order
            print("\nSong list:\n")
            for song in self.playlist:
                print(song)
        else:
            print("There are no songs in your playlist yet.")
    """The Display function loops through and prints each song in the current playlist order."""
player = mediaPlayer()

def menu():
    print(20 * "-", "MENU", 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Sort")
    print("8. Show Currently Playing Song")
    print("9. Show Current Playlist Order")
    print("0. Exit")
    print(46 * "-")

while True:
    menu()
    choice = int(input())
    if choice == 1:
        # Add Song to playlist
        player.addSong()
    elif choice == 2:
        # Remove a song from playlist
        player.removeSong()
    elif choice == 3:
        # Play the playlist from the beginning
        player.playSong()
        # Display song name that is currently playing

    elif choice == 4:
        # Skip to the next song on the playlist
        player.skipSong()
        # Display song name that is now playing

    elif choice == 5:
        # Go back to the previous song on the playlist
        player.prevSong()
        # Display song name that is now playing

    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        player.shuffle()
    elif choice == 7:
        # Sort the playlist alphabetically by the title
        player.sortPlaylist()
    elif choice == 8:
        # Display the song name and artist of the currently playing song
        player.currentlyPlaying()
    elif choice == 9:
        # Display the current order of the playlist
        player.displayPlaylist()
    elif choice == 0:
        print("Goodbye.")
        break