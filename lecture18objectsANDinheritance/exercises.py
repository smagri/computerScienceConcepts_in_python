#!/usr/bin/env python3

class Game:
    # parent class
    name = ""
    numplayers = 2

    def print(self):
        print(self.name)
        pirnt("Up to ", self.numplayers, "players")
    


class Videogame(Game):
    platform = "playstation4"
    name = "video"
    numplayers = 4 # using self.memeberVariableName will indicate this
                   # object only???
    
    def print(self):
        print("Game Name:", self.name)
        print("Video Game platform is: ", self.platform)
        print("Up to ", self.numplayers, "players")



class Boardgame:
    num_pieces = 24
#    borad_size_LxW[2] = [0,0] #list of 2 numbers
    name = "board"
    numplayers = 2
    
    def print(self):
        print("Game Name:", self.name)
 #       print("Board Game lengthXwidth: ", self.board_size_LxW[0], self.board_size_LxW[1])
        print("Number of pieces in the Board Game: ", self.num_pieces)
        print("Up to ", self.numplayers,  "players allowed.")



vgame0 = Videogame()
print("ex3: print a video game's details:")
vgame0.print()
vgame0Name = print(vgame0.name)

print("ex3: print a board game's details:")
brdgame0 = Boardgame()
brdgame0.print()

# ignoring pickle module for now, just using normal python io,
# probably more portable that way - not that easy to do
infileHandle = open("Game.dat", "w") # open&/create file that can be written to
#for i in range():
#infileHandle.write(print(vgame0Name))


# get a line from the file
#savedgame = Videogame()

#infileHandle.close
