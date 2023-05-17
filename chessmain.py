"""
for handling user input and displaying current game state
"""
import pygame as p
import chessengine
width=height=512
dimension=8
sq_size=height//dimension
max_fps=15
images={}
'''
initialzation a golbal dir of images
'''
def loadimages():
    pieces=["bR","bN","bB","bQ","bK","bp","wR","wN","wB","wQ","wK","wp"]
    for piece in pieces:
        images[piece]=p.transform.scale(p.image.load("icons/"+piece+".png"),(sq_size,sq_size))

"""
main driver for code.This will handel user input and updating the graphics
"""
def main():
    p.init()
    screen=p.display.set_mode((width,height))
    clock=p.time.Clock()
    screen.fill(p.Color("white"))
    gs=chessengine.GameState()
    loadimages()
    running=True
    while running:
        for e in p.event.get():
            if e.type==p.QUIT:
                running=False
        drawGamestate(screen,gs)
        clock.tick(max_fps)
        p.display.flip()
"""
responsible for all the graphics within a current game state 
"""
def drawGamestate(screen,gs):
    drawboard(screen)
    drawpieces(screen,gs.board)

'''
draw sqares in the board
'''
def drawboard(screen):
    colors=[p.Color("white"),p.Color("gray")]
    switch=0
    for r in range(dimension):
        for c in range(dimension):
            color=colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*sq_size,r*sq_size,sq_size,sq_size))
'''
draw the pices in the board
'''
def drawpieces(screen,board):
    for r in range(dimension):
        for c in range(dimension):
            piece=board[r][c]
            if piece !="--":
                screen.blit(images[piece],p.Rect(c*sq_size,r*sq_size,sq_size,sq_size))

if __name__ == "__main__":
    main()