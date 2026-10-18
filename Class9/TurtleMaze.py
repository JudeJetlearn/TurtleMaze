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
ending = []

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
                end = turtle.Turtle()
                end.shape("circle")
                end.color("green")
                end.speed(0)
                end.penup()
                end.goto(screenX,screenY)
                ending.append(end)

GameOver = False
StartingTime = time.time()

def EndingColide():
    global GameOver
    PlayerX = player.xcor()
    PlayerY = player.ycor()

    for i in range(len(ending)):
        EndX = ending[i].xcor()
        EndY = ending[i].ycor()

        if PlayerX == EndX and PlayerY == EndY :
            GameOver = True
        elif PlayerX != EndX or PlayerY != EndY :
            GameOver = False

    if GameOver == True:
        screen.bye()
        EndingTime = time.time()
        Duration = EndingTime - StartingTime
        Duration = round(Duration)
        print("Welldone! You have solved the maze.")
        print(f"Time taken: {Duration} seconds.")

def Player_Up():
    PlayerX = player.xcor()
    PlayerY = player.ycor() + 24
    move = True
    
    for i in range(len(blocks)):
        BlockX = blocks[i].xcor()
        BlockY = blocks[i].ycor()
        if PlayerX == BlockX and PlayerY == BlockY :
            move = False

    if move == True:
        player.goto(PlayerX,PlayerY)
        EndingColide()

def Player_Down():
    PlayerX = player.xcor()
    PlayerY = player.ycor() - 24
    move = True
    
    for i in range(len(blocks)):
        BlockX = blocks[i].xcor()
        BlockY = blocks[i].ycor()
        if PlayerX == BlockX and PlayerY == BlockY :
            move = False

    if move == True:
        player.goto(PlayerX,PlayerY)
        EndingColide()

def Player_Right():
    PlayerX = player.xcor() + 24
    PlayerY = player.ycor()
    move = True
    
    for i in range(len(blocks)):
        BlockX = blocks[i].xcor()
        BlockY = blocks[i].ycor()
        if PlayerX == BlockX and PlayerY == BlockY :
            move = False

    if move == True:
        player.goto(PlayerX,PlayerY)
        EndingColide()
    
def Player_Left():
    PlayerX = player.xcor() - 24
    PlayerY = player.ycor()
    move = True
        
    for i in range(len(blocks)):
        BlockX = blocks[i].xcor()
        BlockY = blocks[i].ycor()
        if PlayerX == BlockX and PlayerY == BlockY :
            move = False
            
    if move == True:
        player.goto(PlayerX,PlayerY)
        EndingColide()

screen.listen()
screen.onkey(Player_Up,"Up")
screen.onkey(Player_Down,"Down")
screen.onkey(Player_Right,"Right")
screen.onkey(Player_Left,"Left")

player.goto(-201,201)
MazeMaker()
screen.mainloop()