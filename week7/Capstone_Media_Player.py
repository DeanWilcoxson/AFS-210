import random
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

    def shuffle(self):
        list = self.items
        if len(list) <= 0:
            return None
        elif len(list) == 1:
            return list
        else:
            for index in range(len(list)-1, 0, -1):
                randIndex = random.randint(0, index)
                list[index], list[randIndex] = list[randIndex], list[index]
            return list

    def rotate(self, n):
        if len(self.items) <= 0:
            return None
        elif len(self.items) == 1:
            return self.items
        else:
            if n > 0:
                for _ in range(n):
                    this = self.pop()
                    self.appendLeft(this)
            elif n < 0:
                for _ in range(n):
                    that = self.popLeft()
                    self.append(that)

    def sort(self):
        self.items.sort()

    def peek(self):
        return self.items[0]

    def peekAtIndex(self, index):
        return self.items[index]
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
        self.playState = False

        # Preloaded Songs
        self.playlist.append(Song("Mockingbird", "Eminem"))
        self.playlist.append(Song("Superman", "Eminem"))
        self.playlist.append(Song("Criminal", "Eminem"))
        self.playlist.append(Song("Wherever I May Roam", "Metallica"))
        self.playlist.append(Song("Fade to Black", "Metallica"))
        self.playlist.append(Song("My Friend of Misery", "Metallica"))
        self.playlist.append(
            Song("Walk A Little Straighter", "Billy Currington"))
        self.playlist.append(Song("You're Gonna Miss This", "Trace Adkins"))
        self.playlist.append(Song("Ignition", "Downlink"))
        self.playlist.append(Song("Best Of You", "Foo Fighters"))
    """self.playlist is pointing to the deque as its abstract data structure (Built upon a list). 
       self.playstate is a boolean value to determine whether the media player is 'playing' a song or not.
    """

    def isPlaying(self):
        return self.playState
    """The isplaying function returns a boolean value for the attribute playState."""

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
                print(count+1, ":", i)
                count += 1
            # Prompt user for Song Index
            index = int(input("Remove which track: "))
            # remove song from playlist
            self.playlist.removeAtIndex(index-1)
            print("Song Removed from Playlist")
        else:
            print("There are no songs in your playlist yet.")
    """The removeSong function loops through and displays the playlist and a user input decides which index is removed"""

    def playSong(self):
        # Play the playlist from the beginning
        self.playState = True
        # Display song name that is currently playing
        print("Playing....", self.playlist.peek())
    """The playSong function changes the playState of the application to true and diplays the first item in the list."""

    def skipSong(self):
        # Skip to the next song on the playlist
        print("Next....")
        self.playlist.rotate(1)
        # Display song name that is now playing
        print("Now Playing....", self.playlist.peek())
    """The skipSong Function calls the rotate function that takes a positive integer value as a parameter and pops off the beginning of the list and makes it the last index."""

    def prevSong(self):
        # Go back to the previous song on the playlist
        print("Previous....")
        self.playlist.rotate(-1)
        # Display song name that is now playing
        print("Now Playing....", self.playlist.peek())
    """The prevSong Function calls the rotate function that takes a negative integer value as a parameter and pops off the end of the list and makes it the first index."""

    def shuffle(self):
        if len(self.playlist.items):
            print("Shuffling....")
            self.playlist.shuffle()
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
            if self.isPlaying():
                print(self.playlist.peek())
            else:
                print("No song currently playing.")
        else:
            print("There are no songs in your playlist yet.")
    """The currently playing function calls two functions, isPlaying, and peek. It calls the isPlaying function to check the playState of the mediaPlayer. It calls the peek method of the deque to receive the first item in the deque. Currently playing will always be the 0 index in a deque"""

    def displayPlaylist(self):
        if len(self.playlist.items):
            count = 0
            # Show the current song list order
            print("\nSong list:\n")
            for song in self.playlist:
                count += 1
                print(count, ":", song)
        else:
            print("There are no songs in your playlist yet.")
    """The Display function loops through and prints each song in the current playlist order."""


player = mediaPlayer()


def menu():
    print(20 * "-", "MENU", 20 * "-")
    print("1. Add a Song")
    print("2. Remove a song")
    print("3. Play")
    print("4. Skip Song")
    print("5. Previous Song")
    print("6. Shuffle")
    print("7. Sort")
    print("8. Current Song")
    print("9. Playlist Order")
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
    elif choice == 4:
        # Skip to the next song on the playlist
        player.skipSong()
    elif choice == 5:
        # Go back to the previous song on the playlist
        player.prevSong()
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
