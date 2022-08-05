#imports
import pygame as pg
import sys


#initialisation of pygame and window
winSize = (800,800) 
pg.init()
win = pg.display.set_mode(winSize)
clock = pg.time.Clock()

#loading a starting generation from "start.txt"
try:
    game = []
    with open("start.txt","r") as file:
        contents= True
        while contents != "":
            contents=file.readline()
            contents=contents.strip()
            splitContents=contents.split(",")
            if len(splitContents)==1:  #end of file condition
                break
            else:
                for i in range(len(splitContents)):
                    splitContents[i] = int(splitContents[i])
            game.append(splitContents)

#creating a new file called "start.txt" which will be filled with 0's
except:
    #dividing resolution into cells with floor division of the window size
    game = []
    for i in range(winSize[0]//10):
        row = []
        for j in range(winSize[0]//10):
            row.append(0)
        game.append(row)

    #writing the rows of 0's into the file
    with open("start.txt","w") as file:
        for i in game:
            line = ""
            for j in range(len(i)):
                if j == len(i)-1:
                    line += str(i[j])
                else:
                    line+= str(i[j]) + ","
            file.write(line)
            file.write("\n")
        

        


#debug generation printer
def pTemp(temp):
    for i in temp:
        print(i)





class Game:
    #Initialising game of life window with the first generation
    def __init__(self, window, size):
        self.size = size
        self.window = window


    #The rule checking and generation updating function that checks for the all cells if they should live or die in the next generation
    def check(self):
        #creating a copy of the last generation
        temp = []
        for i in self.window:
            l = []
            for j in i:
                l.append(j)
            temp.append(l)

        #storing resolution of cells
        yMax = len(temp)
        xMax = len(temp[0])

        #updating each cell according to the rules of Conway's game of life
        for row in range(len(temp)):
            for column in range(len(temp[row])):
                counter = 0
                for i in range(3):
                    for j in range(3):
                        #sum of all the cells alive in the 3x3 grid with the current cell at its center (including itself)
                        counter += temp[(row - 1 + i) % yMax][(column - 1 + j) % xMax]

                        #old solution for checking the numbers of neighbours alive for each cell
                        """
                        x= i-1
                        y= j-1
                        if not(x==0 and y==0):
                            try:
                                if temp[row+x][column+y] == 1:
                                    
                                    counter += 1
                            except:
                                pass"""
                #subtracting the value of the cell being checked from the sum of the 3x3 grid to give sum of neighbours alive
                counter -= temp[row][column]

                #assigning dead or alive states for each cell
                if counter <2 or counter >3:
                    self.window[row][column] = 0
                if counter == 3:
                    self.window[row][column] = 1


    #drawing function for pygame window that is run every frame
    def draw(self):

        #drawing each cell as white if alive, black if dead on the pygame window
        for row in range(len(self.window)):
            for column in range(len(self.window[row])):
                if self.window[row][column] == 1:
                    pg.draw.rect(win, (255,255,255),( row*self.size, column*self.size, self.size, self.size))

        #updating the last generation
        self.check()
        
                            
#setting run to true so that it enters the while loop
run = True
#creating the game class object
newGame = Game(game,10)

#game loop that draws the pygame screen and updates it each frame
while run:
    #10 frames per second
    clock.tick(10)
    #filling screen with black
    win.fill((0,0,0))

    #event handler to check if the window is closed
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            sys.exit()

    #window draw and update
    newGame.draw() 
    pg.display.update()
    
