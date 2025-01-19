from API import * 
import sys
from time import sleep

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

class cell:
    def __init__(self,x,y,score):#walls pattern nesw
        self.wall=[0,0,0,0]
        self.parent=None
        self.x=x
        self.y=y
        self.hit=False
        self.score=score

dist=[]
track=[]


def updatedist():
    global dist
    # log("yo")
    tobechecked=[dist[7][7],dist[8][7],dist[7][8],dist[8][8]]
    # for i in dist :
    #     for j in i:
    #         j.score=0
    for k in [dist[7][7],dist[8][7],dist[7][8],dist[8][8]]:
        k.hit=True
    while len(tobechecked)!=0:
        pointer=tobechecked.pop()
        
            
            
        # Check north direction
        try:
            # if pointer==dist[7][15]:

            #     # log("worked")
            if dist[pointer.y - 1][pointer.x].hit == False and dist[pointer.y][pointer.x].wall[0] == 0 :#and dist[pointer.y][pointer.x].score!=0 :
                dist[pointer.y - 1][pointer.x].hit = True
                tobechecked.insert(0, dist[pointer.y - 1][pointer.x])
                dist[pointer.y - 1][pointer.x].score = pointer.score + 1
        except IndexError:
            pass    
                # log("up")
            # Check east direction
        try:
            if dist[pointer.y][pointer.x + 1].hit == False and dist[pointer.y][pointer.x].wall[1] == 0 :#and dist[pointer.y][pointer.x].score!=0:
                dist[pointer.y][pointer.x + 1].hit = True
                tobechecked.insert(0, dist[pointer.y][pointer.x + 1])
                dist[pointer.y][pointer.x + 1].score = pointer.score + 1
                # log("right")
        except IndexError:
            pass
            # Check sout
            # h direction
        try:
            if dist[pointer.y + 1][pointer.x].hit == False and dist[pointer.y][pointer.x].wall[2] == 0: #and dist[pointer.y][pointer.x].score!=0:
                dist[pointer.y + 1][pointer.x].hit = True
                tobechecked.insert(0, dist[pointer.y + 1][pointer.x])
                dist[pointer.y + 1][pointer.x].score = pointer.score + 1
                # log("down")
        except IndexError:
            pass
        try:
            # Check west direction
            if dist[pointer.y][pointer.x - 1].hit == False and dist[pointer.y][pointer.x].wall[3] == 0:# and dist[pointer.y][pointer.x].score!=0:
                dist[pointer.y][pointer.x - 1].hit = True
                tobechecked.insert(0, dist[pointer.y][pointer.x - 1])
                dist[pointer.y][pointer.x - 1].score = pointer.score + 1
                # log("left")
        except IndexError:
            pass
            if pointer==dist[7][14]:
                log("error")
            # log("errorerrorerror")
    
    o=[]
    for i in dist :
        o.append([])
        for j in i:
            j.hit=False
            o[-1].append(j.score)
    # log(str(o))        

def finish():  
    global track 
    log(str("---->")+str(track))  
    seter=dist[counter[1]][counter[0]]                      
    while 1:
        if seter.parent ==None:
            break
        setColor(seter.x,15-seter.y,"g")
        seter=seter.parent 
        
    #write a function add two numbers
    


def main():
    global dist,track,counter
    
    for i in range(16):
        dist.append([])
        for j in range(16):

            dist[i].append(cell(j,i,abs(i-7)-int((j)/8)-int((i)/8)+abs(j-7)))

    for i in range(16):
        dist[0][i].wall[0]=1
        dist[i][0].wall[3]=1
    counter=[0,15]
    orientation=0
    for i in range(16):
        for j in range(16):
            setText(i,j,str(dist[i][j].score))
    setColor(0, 0, "b") 
    while True:
        if orientation>270:
            orientation=orientation%360
        elif orientation<0:
            orientation+=360
        log (str(track))
        track.append([counter[0],counter[1]])
        for i in range(16):
            for j in range(16):
                setText(j,15-i,str(dist[i][j].score))
                p=0
                for k in list("nesw"):
                    if dist[i][j].wall[p]  :
                        setWall(j,15-i,k)  
                    p+=1    
        cvalue=dist[counter[1]][counter[0]].score
        if cvalue==0:
            
            finish()
            break

        # if wallFront():
        #     dist[counter[1]][counter[0]].wall=bytes(2**(orientation/90))
            
        # if wallRight():
        #     if orientation==270:
        #         dist[counter[1]][counter[0]].wall=0b0001
                
        #     else:
        #         dist[counter[1]][counter[0]].wall=bytes(2**((orientation+90)/90))
        # if wallLeft():
        #     if orientation==0:
        #         dist[counter[1]][counter[0]].wall=0b1000
        #     else:
        #         dist[counter[1]][counter[0]].wall=bytes(2**((orientation-90)/90))
        # log(str (orientation))
        if (orientation == 90 and wallLeft()) or (orientation == 270 and wallRight()) or (wallFront() and orientation == 0) or (orientation==180 and wallBack()):
            dist[counter[1]][counter[0]].wall[0] = 1
            updatedist()
            # Mark the north wall of the current cell
            try :
                dist[counter[1] - 1][counter[0]].wall[2] = 1  # Mark the south wall of the cell above
            except:
                pass
        if (orientation == 180 and wallLeft()) or (orientation == 0 and wallRight()) or (wallFront() and orientation == 90)or (orientation==270 and wallBack()):
            dist[counter[1]][counter[0]].wall[1] = 1
            updatedist()
                # Mark the east wall of the current cell
            try:
                dist[counter[1]][counter[0] + 1].wall[3] = 1  # Mark the west wall of the cell to the right
            except:
                pass
        if (orientation == 270 and wallLeft()) or (orientation == 90 and wallRight()) or (wallFront() and orientation == 180)or (orientation==0 and wallBack()):
            dist[counter[1]][counter[0]].wall[2] = 1
                # Mark the south wall of the current cell
            updatedist()
            try:
                dist[counter[1] + 1][counter[0]].wall[0] = 1  # Mark the north wall of the cell below
            except:
                pass
            
        if (orientation == 0 and wallLeft()) or (orientation == 180 and wallRight()) or (wallFront() and orientation == 270) or (orientation==90 and wallBack()):
            dist[counter[1]][counter[0]].wall[3] = 1  # Mark the west wall of the current cell
            updatedist()
            try:
                dist[counter[1]][counter[0] - 1].wall[1] = 1  # Mark the east wall of the cell to the left
            except:
                pass
         
        if not wallFront():
            # log("-----------------------------------")
            if orientation==0 and  dist[counter[1]-1][counter[0]].score<=cvalue: 
                # log("11")
                
                counter[1]-=1
                # dist[counter[1]-1][counter[0]].parent=dist[counter[1]][counter[0]]
                moveForward()
                 
                continue
            elif orientation==90 and dist[counter[1]][counter[0]+1].score<=cvalue:
                # log("22")
                
                counter[0]+=1
                # dist[counter[1]][counter[0]+1].parent=dist[counter[1]][counter[0]]
                moveForward()
                 
                continue
            elif orientation==180 and dist[counter[1]+1][counter[0]].score<=cvalue:
                counter[1]+=1
                moveForward()
                # dist[counter[1]+1][counter[0]].parent=dist[counter[1]][counter[0]]
                # log("33")
                continue
            elif orientation==270 and dist[counter[1]][counter[0]-1].score<=cvalue:
            
                counter[0]-=1
                moveForward()
                # dist[counter[1]][counter[0]-1].parent=dist[counter[1]][counter[0]]
                # log("44")
                continue
            
        if not wallLeft():
            if orientation==90: 
                if dist[counter[1]-1][counter[0]].score<=cvalue:
                    counter[1]-=1
                    turnLeft()
                    moveForward()
                    orientation-=90
                    # dist[counter[1]-1][counter[0]].parent=dist[counter[1]][counter[0]]
                     
                    continue
            elif orientation==180:
                if dist[counter[1]][counter[0]+1].score<=cvalue:
                    counter[0]+=1
                    turnLeft()
                    moveForward()
                    orientation-=90
                    # dist[counter[1]][counter[0]+1].parent=dist[counter[1]][counter[0]]
                     
                    continue
            elif orientation==270:
                if dist[counter[1]+1][counter[0]].score<=cvalue:
                    counter[1]+=1
                    turnLeft()
                    moveForward()
                    orientation-=90
                    # dist[counter[1]+1][counter[0]].parent=dist[counter[1]][counter[0]]
                    continue
            elif orientation==0:
                if dist[counter[1]][counter[0]-1].score<=cvalue:
                    counter[0]-=1
                    turnLeft()
                    moveForward()
                    orientation-=90
                    # dist[counter[1]][counter[0]-1].parent=dist[counter[1]][counter[0]]
                    continue
            
        if not wallRight():
            
            if orientation==270: 
                if dist[counter[1]-1][counter[0]].score<=cvalue:
                    counter[1]-=1
                    turnRight()
                    moveForward()
                    orientation+=90
                    # dist[counter[1]-1][counter[0]].parent=dist[counter[1]][counter[0]]
                    continue
            elif orientation==0:

                if dist[counter[1]][counter[0]+1].score<=cvalue:
                    counter[0]+=1
                    turnRight()
                    moveForward()
                    orientation+=90
                    # dist[counter[1]][counter[0]+1].parent=dist[counter[1]][counter[0]]
                    continue
            elif orientation==90:
                if dist[counter[1]+1][counter[0]].score<=cvalue:
                    counter[1]+=1
                    turnRight()
                    moveForward()
                    orientation+=90
                    # dist[counter[1]+1][counter[0]].parent=dist[counter[1]][counter[0]]
                    continue
            elif orientation==180:
                if dist[counter[1]][counter[0]-1].score<=cvalue:
                    counter[0]-=1
                    turnRight()
                    moveForward()
                    orientation+=90
                    # dist[counter[1]][counter[0]-1].parent=dist[counter[1]][counter[0]]
                     
                    continue
        if not wallBack():
            if orientation==270: 
                if dist[counter[1]][counter[0]+1].score<=cvalue:
                    counter[0]+=1
                    turnRight()
                    turnRight()
                    moveForward()
                    orientation=90
                    # dist[counter[1]][counter[0]+1].parent=dist[counter[1]][counter[0]]
                    continue
            elif orientation==0:

                if dist[counter[1]+1][counter[0]].score<=cvalue:
                    counter[1]+=1
                    turnRight()
                    turnRight()
                    moveForward()
                    orientation=180
                    # dist[counter[1]+1][counter[0]].parent=dist[counter[1]][counter[0]]
                    continue
            elif orientation==90:
                if dist[counter[1]][counter[0]-1].score<=cvalue:
                    counter[0]-=1
                    turnRight()
                    turnRight()
                    moveForward()
                    orientation=270
                    # dist[counter[1]][counter[0]-1].parent=dist[counter[1]][counter[0]]
                    continue
            elif orientation==180:
                if dist[counter[1]-1][counter[0]].score<=cvalue:
                    counter[1]-=1
                    turnRight()
                    turnRight()
                    moveForward()
                    orientation=0
                    # dist[counter[1]-1][counter[0]].parent=dist[counter[1]][counter[0]]
                    continue
        
        updatedist()
            
                
        

      
        

if __name__ == "__main__":
    main()
