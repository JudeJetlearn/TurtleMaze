import turtle
import time

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width = 500, height = 500 )

turtle.speed(0)
turtle.shape("square")
turtle.penup()

Maze = [
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
            if charater == "F":
                block = turtle.Turtle()
                block.shape("circle")
                block.color("green")
                block.speed(0)
                block.penup()
                block.goto(screenX,screenY)


MazeMaker()
screen.mainloop()