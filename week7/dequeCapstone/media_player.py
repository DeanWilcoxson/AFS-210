# from playsound import playsound
# import media_files
def myFunc(e):
    return e['artist']

class NewDoubleEndedQueue():
    def __init__(self):
        self.items = []

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

    def removeAtIndex(self, item):
        self.items.remove(item)

    def reverse(self):
        self.items.reverse()

    def rotate(self):
        self.items = self.items[len(self.items)//3:] + \
            self.items[:len(self.items)//3]
        return self.items

    def sort(self):
        self.items.sort(key=myFunc)


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        # self.link = link

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    # def getLink(self):
    #     return self.link

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


def menu():
    print(20 * "-", "MENU", 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


while True:
    menu()
    choice = int(input())
    deque = NewDoubleEndedQueue()
    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        songName = input("Song Title: ")
        songArtist = input("Artist Name: ")
        song = Song(songName, songArtist)
        print(song)
        # Add song to playlist
        deque.items.append(song)
        print(deque.items)
        print(f"{song} Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title
        title = input("Please Enter Song Title: ")
        # remove song from playlist
        deque.removeAtIndex(title)
        print(f"{title}Song Removed from Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        playsound(
            'C:\\Users\\Gainious\\Dev\\bryanu\\AFS-210\\week7\\dequeCapstone\\media_files\\SF2-Guile.mp3')
        # Display song name that is currently playing
        print("Playing....")
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
    elif choice == 0:
        print("Goodbye.")
        break
