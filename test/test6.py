class Playlist:
    def __init__(self,name):
        self.name=name
        self.songs =[]

    def addSong(self,song):
        self.songs.append(song)

    def removeSong(self,song):
        if song in self.songs:
            self.songs.remove(song)
            return 1
        else:
            return 0

    def __str__(self):
        ans = ''
        for song in self.songs:
            ans = ans + '-'+song+'\n'
        return ans

    def show(self):
        print(self.name)
        print(self.__str__())

p1 = Playlist('Pravin')
p1.addSong('Sanso ki mala')
p1.addSong('Headlights')

p1.show()

p1.removeSong('Headlights')
p1.show()
