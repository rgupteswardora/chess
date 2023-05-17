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
        clock.tick(max_fps)
        p.display.flip()

if __name__ == "__main__":
    main()