#put the pointer on the canvas(white area),to make walls click the left mouse button,to remove them use right mouse button,
# for the START and END nodes use s and e keys respectively.(NOTE:to remove the the start or end nodes use s or e keys respectively or use right mouse button)
# to start the algorithm press c 
#also there is a bug so dont go too left
from tkinter import *
import turtle                 
import time
import sys
from collections import deque
global root
root=Tk()
c=Canvas(root,height=560,width=840,bg="white")
c.place(x=70,y=70)
global endl
endl=71

s_check=True
e_check=True
li=list("+                                         +" for i in range(27))
li.insert(0,"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
li.insert(28,"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

                                                                                                            
def printq(events):   
    global s_check,e_check
    c.create_rectangle (x2,y2,x2+w,y2+w,fill="black",outline="white")

    my=li[liy]
    k=my[0:lix]+"+"+my[lix+1:endl]
    if my[lix]=="s":
        s_check=True
    if my[lix]=="e":
        e_check=True
    li[liy]=k
def motion(event):
    global x2
    global y2
    global w,lix,liy
    x, y = event.x, event.y
    w=20
    x2=(x//20)*20
    y2=(y//20)*20
    liy=int(y2/20)
    lix=int(x2/20)
def createit(events):
    wn = turtle.Screen()               # define the turtle screen
    wn.bgcolor("white")                # set the background colour
    wn.title("A BFS Maze Solving Program")
    wn.setup(1300,700)                  # setup the dimensions of the working window


    # this is the class for the Maze
    class Maze(turtle.Turtle):               # define a Maze class
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")            # the turtle shape
            self.color("black")             # colour of the turtle
            self.penup()                    # lift up the pen so it do not leave a trail
            self.speed(0)

    # this is the class for the finish line - green square in the maze
    class Green(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("cyan")
            self.penup()
            self.speed(0)

    class Blue(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("blue")
            self.penup()
            self.speed(0)


    # this is the class for the yellow or turtle
    class Red(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("red")
            self.penup()
            self.speed(0)

    class Yellow(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("aquamarine2")
            self.penup()
            self.speed(0)



    def setup_maze(grid):                          # define a function called setup_maze
        global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
        for y in range(len(grid)):                 # read in the grid line by line
            for x in range(len(grid[y])):          # read each cell in the line
                character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
                screen_x = -500 + (x * 24)         # move to the x location on the screen staring at -588
                screen_y = 340 - (y * 24)          # move to the y location of the screen starting at 288

                if character == "+":
                    maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                    maze.stamp()                          # stamp a copy of the turtle on the screen
                    walls.append((screen_x, screen_y))    # add coordinate to walls list

                if character == " " or character == "e":
                    path.append((screen_x, screen_y))     # add " " and e to path list

                if character == "e":
                    green.color("purple")
                    green.goto(screen_x, screen_y)       # send green sprite to screen location
                    end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                    green.stamp()
                    green.color("cyan")

                if character == "s":
                    start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                    red.goto(screen_x, screen_y)


    def endProgram():
        wn.exitonclick()
        sys.exit()

    def search(x,y):
        frontier.append((x, y))
        solution[x,y] = x,y

        while len(frontier) > 0:          # exit while loop when frontier queue equals zero
            time.sleep(0)
            x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

            if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
                cell = (x - 24, y)
                solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
                #blue.goto(cell)        # identify frontier cells
                #blue.stamp()
                frontier.append(cell)   # add cell to frontier list
                visited.add((x-24, y))  # add cell to visited list

            if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
                cell = (x, y - 24)
                solution[cell] = x, y
                #blue.goto(cell)
                #blue.stamp()
                frontier.append(cell)
                visited.add((x, y - 24))
                print(solution)

            if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
                cell = (x + 24, y)
                solution[cell] = x, y
                #blue.goto(cell)
                #blue.stamp()
                frontier.append(cell)
                visited.add((x +24, y))

            if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
                cell = (x, y + 24)
                solution[cell] = x, y
                #blue.goto(cell)
                #blue.stamp()
                frontier.append(cell)
                visited.add((x, y + 24))
            green.goto(x,y)
            green.stamp()


    def backRoute(x, y):
        yellow.goto(x, y)
        yellow.stamp()
        while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
            yellow.goto(solution[x, y])        # move the yellow sprite to the key value of solution ()
            yellow.stamp()
            x, y = solution[x, y]               # "key value" now becomes the new key

    # set up classes
    maze = Maze()
    red = Red()
    blue = Blue()
    green = Green()
    yellow = Yellow()

    # setup lists
    walls = []
    path = []
    visited = set()
    frontier = deque()
    solution = {}                           # solution dictionary


    # main program starts here ####
    setup_maze(li)
    search(start_x,start_y)
    backRoute(end_x, end_y)
    wn.exitonclick()
    root.destroy()
def s_point(events):
    global s_check
    my=li[liy]
    kt=my[lix]
    if s_check==True:
        c.create_rectangle (x2,y2,x2+w,y2+w,fill="blue",outline="white")

        
        k=my[0:lix]+"s"+my[lix+1:endl]
        li[liy]=k
        s_check=False
    elif s_check==False and kt=="s":
        c.create_rectangle (x2,y2,x2+w,y2+w,fill="white",outline="white")
        

        s_check=True
        k=my[0:lix]+"s"+my[lix+1:endl]
        li[liy]=k
def e_point(events):
    global e_check
    my=li[liy]
    kt=my[lix]
    if e_check==True:
        c.create_rectangle (x2,y2,x2+w,y2+w,fill="purple",outline="white")

        
        k=my[0:lix]+"e"+my[lix+1:endl]
        li[liy]=k
        e_check=False
    elif e_check==False and kt=="e":
        c.create_rectangle (x2,y2,x2+w,y2+w,fill="white",outline="white")
        


        e_check=True
        k=my[0:lix]+"e"+my[lix+1:endl]
        li[liy]=k
def chemp2(events):  
    global s_check,e_check
    c.create_rectangle(x2,y2,x2+w,y2+w,fill="white",outline="white")
    my=li[liy]
    k=my[0:lix]+" "+my[lix+1:endl]
    if my[lix]=="s":
        s_check=True
    if my[lix]=="e":
        e_check=True
    li[liy]=k

b34=Button(root,text="create",command=createit)
b34.place(x=4000,y=630)
root.bind('c', createit)
root.bind('s', s_point)
root.bind('e', e_point)
c.bind('<Motion>', motion)
root.bind('<B1-Motion>', printq)
root.bind('<Button-1>', printq)




root.bind('<B3-Motion>', chemp2)
c.bind('<Button-3>', chemp2)

root.geometry("1000x1000")
root.mainloop()
print(li)
#by mithil singh

