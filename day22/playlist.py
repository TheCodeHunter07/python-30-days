# ASSIGNMENT
# 3 playlist.py — a Playlist class that supports len(playlist)

class Playlist:

    def __init__(self,songs):
          
          self.songs = songs

    def __len__(self):

         return len(self.songs)


playlist = Playlist(["Believer", "Perfect", "Memories"])

print(len(playlist))