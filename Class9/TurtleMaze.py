import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width = 500, height = 500 )

Maze = [
    "XXXXXXXXXXXXXXX",
    "X             X",
    "XXXXXXXXXXXXX X",
    "X   X X     X X",
    "X X X X XXX X X",
    "X X      X    X",
    "X XXXXXXXXXXXXX",
    "X X     XF    X",
    "X X XXX XXXXX X",
    "X   X   X   X X",
    "XXXXX XXX X X X",
    "X         X   X",
    "XXXXXXXXXXXXXXX"
]

Maze2 = [
    "XXXXXXXXXXXXXXX",
    "X   X         X",
    "X XXXXX XXXXX X",
    "X X     X     X",
    "X X XXX X XXX X",
    "X X   X X X   X",
    "X XXX X X X XXX",
    "X     X X X   X",
    "XXXXX X X X XXX",
    "X     X   X   X",
    "X XXXXX XXXXX X",
    "X             X",
    "XXXXXXXXXXXXX F"
]

player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.speed(0)
player.penup()

blocks = []

def MazeMaker():
    for y in range(len(Maze)):
        for x in range(len(Maze[y])):
            charater = Maze[y][x]
            screenX = -225 + (x * 24)
            screenY = 225 - (y * 24)
            if charater == "X":
                block = turtle.Turtle()
                block.shape("square")
                block.color("black")
                block.speed(0)
                block.penup()
                block.goto(screenX,screenY)
                blocks.append(block)
            if charater == "F":
                block = turtle.Turtle()
                block.shape("circle")
                block.color("green")
                block.speed(0)
                block.penup()
                block.goto(screenX,screenY)

PlayerX = player.xcor()
PlayerY = player.ycor()

def Player_Up():
    PlayerX = player.xcor()
    PlayerY = player.ycor()+24
    move = True
    
    for i in range(len(blocks)):
        BlockY = blocks[i].ycor()
        if PlayerY == BlockY:
            move = False
    if move == True:
        player.goto(PlayerX,PlayerY)

def Player_Down():
    PlayerY = player.ycor()
    player.goto(PlayerX,PlayerY-24)
def Player_Right():
    PlayerX = player.xcor()
    player.goto(PlayerX+24,PlayerY)
def Player_Left():
    PlayerX = player.xcor()
    player.goto(PlayerX-24,PlayerY)

screen.listen()
screen.onkey(Player_Up,"Up")
screen.onkey(Player_Down,"Down")
screen.onkey(Player_Right,"Right")
screen.onkey(Player_Left,"Left")


player.goto(-201,201)
MazeMaker()
screen.mainloop()