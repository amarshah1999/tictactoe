#imports
import pygame
from sys import exit
#setup
win = pygame.display.set_mode((300,300))
pygame.display.set_caption("tictactoe")
circle = pygame.image.load('circle.png')
cross = pygame.image.load('cross.png')
box = pygame.image.load('square.png')

#classes
class square(pygame.sprite.DirtySprite):
    def __init__(self, row, column):
        pygame.sprite.DirtySprite.__init__ (self)
        self.r = row
        self.c = column
        self.state = "n"
        self.hitbox = pygame.Rect(column*100, row*100, 100, 100)
        win.blit(box, (column*100, row*100))
        pygame.display.flip()
        
     
class board:
    
    def __init__(self):
        self.gridarray=[[0,0,0],[0,0,0],[0,0,0]]
        self.turn = 1
        for i in range(0,3):
            for j in range(0,3):
                self.gridarray[i][j] = square(i,j)
                
    def checkwin(self, num, r, c):
        if num == 1:
            playerstate = "o"
        else:
            playerstate = "x"
        #check 3 in a row
        if(self.gridarray[r][(c+1)%3].state == self.gridarray[r][(c+2)%3].state == playerstate):
            print(playerstate + " wins" + " by placing 3 in row " + str(r+1))
            self.endgame()
        #check 3 in a column
        elif(self.gridarray[(r+1)%3][c].state == self.gridarray[(r+2)%3][c].state == playerstate):
            print(playerstate + " wins" + " by placing 3 in column " + str(c+1))
            self.endgame()
        #check diagonal top left to bottom right OR bottom left to top right
        elif(self.gridarray[0][0].state == self.gridarray[1][1].state == self.gridarray[2][2].state) or (self.gridarray[2][0].state == self.gridarray[1][1].state == self.gridarray[0][2].state):
            print(playerstate + " wins by placing 3 diagonally")
            self.endgame()
        
                
    def endgame(self):
        pygame.time.wait(2000)
        main()

    def boxclick(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.gridarray[i][j].hitbox.collidepoint(pygame.mouse.get_pos()):
                    if(self.gridarray[i][j].state == "n"):
                        if self.turn%2 == 1:
                            win.blit(circle, (self.gridarray[i][j].c*100, self.gridarray[i][j].r*100))
                            self.gridarray[i][j].state = "o"
                        elif self.turn%2 == 0:
                            win.blit(cross, (self.gridarray[i][j].c*100, self.gridarray[i][j].r*100))
                            self.gridarray[i][j].state = "x"
                        pygame.display.flip()
                        if (self.turn>4):
                            self.checkwin(self.turn%2, i, j)
                        self.turn+= 1
#main
                      
def main():
    gameboard = board()

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.event.wait().type == pygame.MOUSEBUTTONUP:
                        gameboard.boxclick()
                        

main()
    
