from tkinter import *
from tkinter import messagebox
import random
Match = [None] * 9
winCondition = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
Machine = False
Two = False
XO = 'O' 
D=0
P=0
def newWindow():
 master.destroy()   
 def Mech():
  global Machine,Two,D
  if D==1 and Two==False:    
    Match[0] = 'X'
    draw()
    Machine = True
    Two=False
  elif D==2 and P<2:
    Match[0] = 'X'
    draw()
    Machine = True
    Two=False
 def PresentMoves(node):
    moveArray = []
    for x in range(9):
        if None == node[x]:
            moveArray.append(x)
    return moveArray
 def finish(cell):
    complete = True
    for x in range(9):
        if cell[x] == None:
            complete = False
    if complete:
        return True
    if winner(cell) != None:
        return True
    return False
 def winner(cell):
    for player in ['X', 'O']:
        playerPositions = getSquares(player,cell)
        for combo in winCondition:
            win = True
            for position in combo:
                if position not in playerPositions:
                    win = False
            if win:
                return player
    return None
 def getSquares(player,cell):
    squares = []
    for p in range(9):          
        if cell[p] == player:
            squares.append(p)  
    return squares
 def draw():
    global Match,P
    P=P+1
    c = 0
    for x in range(70, 391, 130):
        for y in range(70, 391, 130):
            if Match[c] == None:
                Xl = ' '
            else:
                Xl = Match[c]
            if Xl == 'X':
                screen.create_text((y,x), font=('bold',100), text = Xl, fill = 'AntiqueWhite', tag='Del')
            else:
                screen.create_text((y,x), font=('bold',100), text = Xl, fill = 'black', tag='Del')
            c += 1
    root.update()
 def TwoPlayer():
    global Two,Machine,XO
    if D==1 and Machine==False:
     Two = True
     Machine=False
     XO = 'O'
 def update(event):
    global Match,XO
    if Machine and Two==False:
        if len(getSquares('X', Match)) != len(getSquares('O', Match)) +1:
            return
    elif Two==False:
        if len(getSquares('X', Match)) != len(getSquares('O', Match)):
            return
    if event.x in range(10, 130) and event.y in range(10, 130):
        if Two == True and Match[0]== None:
            Match[0]=XO
            if XO == 'X':
                XO='O'
            else:
                XO='X'
        elif Match[0] == None:
            Match[0] = 'O'
        else:
            return
    elif event.x in range(141, 260) and event.y in range(10, 130):
         if Two == True and Match[1]== None:
            Match[1]=XO
            if XO == 'X':
                XO='O'
            else:
                XO='X'
         elif Match[1] == None:
            Match[1] = 'O'
         else:
            return
    elif event.x in range(270, 391) and event.y in range(10, 131):
         if Two == True and Match[2]== None:
            Match[2]=XO
            if XO == 'X':
                XO='O'
            else:
                XO='X'
         elif Match[2] == None:
            Match[2] = 'O'
         else:
            return        
    elif event.x in range(10, 131) and event.y in range(140, 260):
         if Two == True and Match[3]== None:
            Match[3]=XO
            if XO == 'X':
                XO='O'
            else:
                XO='X'
         elif Match[3] == None:
            Match[3] = 'O'
         else:
            return    
    elif event.x in range(140, 260) and event.y in range(140, 260):
         if Two == True and Match[4]== None:
            Match[4]=XO
            if XO == 'X':
                XO='O'
            else:
                XO='X'
         elif Match[4] == None:
            Match[4] = 'O'
         else:
            return
    elif event.x in range(270, 391) and event.y in range(140, 260):
         if Two == True and Match[5]== None:
            Match[5]=XO
            if XO == 'X':
                XO='O'
            else:
                XO='X'
         elif Match[5] == None:
            Match[5] = 'O'
         else:
            return
    elif event.x in range(10, 131) and event.y in range(270, 391):
         if Two == True and Match[6]== None:
            Match[6]=XO
            if XO == 'X':
                XO='O'
            else:
                XO='X'
         elif Match[6] == None:
            Match[6] = 'O'
         else:
            return
    elif event.x in range(140, 260) and event.y in range(270,391):
         if Two == True and Match[7]== None:
            Match[7]=XO
            if XO == 'X':
                XO='O'
            else:
                XO='X'
         elif Match[7] == None:
            Match[7] = 'O'
         else:
            return
    elif event.x in range(270, 391) and event.y in range(270, 391):
         if Two == True and Match[8]== None:
            Match[8]=XO
            if XO == 'X':
                XO='O'
            else:
                XO='X'
         elif Match[8] == None:
            Match[8] = 'O'
         else:
            return
    draw()
    if finish(Match):
        endgame()
        return 
    if easy.get() == 0:
     if D==2 and Machine:
        outcome, bestMove = minimax(Match, True)
        Match[bestMove] = 'X'
     elif D==1 and Two==False:
        outcome, bestMove = minimax(Match, True)
        Match[bestMove] = 'X'
    if Two ==False and D==1:
     draw()
    elif Machine==True and D==2:
     draw()
    if finish(Match) and Two==False:
        endgame()
        return
 def endgame():
    global Match
    if winner(Match) == 'X' and Two== False:
        messagebox.showerror('LOSER!', 'You lost!')
    elif winner(Match) == 'O' and Two == False:
        messagebox.showerror('WINNER!!', 'CONGO!')
    elif winner(Match) == 'X' and Two == True:
        messagebox.showerror('CONGO!!','X win')
    elif winner(Match) == 'O' and Two == True:
        messagebox.showerror('CONGO!!','O win')
    else:
        messagebox.showerror('DRAW', 'DRAW!')
 def restart():
    global Match,Two,Machine,XO,P
    if D==2:
     Machine=False
     P=0
     Two=True
    elif D==1:
     Machine=False
     Two=False
    XO='O'
    Match = [None] * 9
    screen.delete('Del')
    draw()
 def makeMove(position, player, cell):
    cell[position] = player
 def minimax(cell, maxPlayer): 
    if finish(cell):
        if winner(cell) == 'X':
            return 1, cell
        elif winner(cell) == 'O':
            return -1, cell
        return 0, cell
    if maxPlayer:
        best = -1
        bestMove = None
        for move in PresentMoves(cell):
            makeMove(move, 'X', cell)
            val, choice = minimax(cell, False)
            makeMove(move, None, cell)
            if val >= best:
                bestMove = move
                best = val
        return best, bestMove
    else:
        best = 1
        bestMove = None
        for move in PresentMoves(cell):
            makeMove(move, 'O', cell)
            val, choice = minimax(cell, True)
            makeMove(move, None, cell)
            if val <= best:
                bestMove = move
                best = val
        return best, bestMove
 def center_window(w,h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
 def MultiPlay():
  global Two,Machine,D
  D=2
  Two=True
  Machine=False
  MachineFirst.pack(side = LEFT, expand = True, fill = BOTH)
  Restart.pack(side = RIGHT, expand = True, fill = BOTH)
  screen.bind('<Button-1>', update)
  screen.create_line(0,133, 400, 133, width = 5)
  screen.create_line(0, 266, 400, 266, width = 5)
  screen.create_line(133, 0, 133, 400, width = 5)
  screen.create_line(266, 0, 266, 400, width = 5)
  screen.pack()
 def OnePlay():
  global Two,Machine,D
  D=1
  Two=False
  MachineFirst.pack(side = LEFT, expand = True, fill = BOTH)
  Restart.pack(side = LEFT, expand = True, fill = BOTH)
  forTwoPlayer.pack(side = LEFT, expand = True, fill = BOTH)
  screen.bind('<Button-1>', update)
  screen.create_line(0,133, 400, 133, width = 5)
  screen.create_line(0, 266, 400, 266, width = 5)
  screen.create_line(133, 0, 133, 400, width = 5)
  screen.create_line(266, 0, 266, 400, width = 5)
  screen.pack()
 root = Tk()
 root.resizable(False,False)
 root.title('TicTacToe')
 root.geometry('406x425')
 center_window(406,425)
 pane = Frame(root) 
 pane.pack(fill = BOTH, expand = True)
 MachineFirst = Button(pane, text='Single Player PC First',bg='bisque2',command=Mech)
 easy = IntVar()
 forTwoPlayer= Button(pane,text='Multi-Player',bg='bisque2',command=TwoPlayer)
 Restart = Button(pane, text='Click to Restart',bg='bisque2',command=restart)
 b1 =Button(root,text='Single-Player',bg='aquamarine',height=1,width=12,command=OnePlay)
 b1.place(relx=0.5,rely=0.4,anchor=CENTER)
 b2 =Button(root,text='Multi-Player',bg='aquamarine',height=1,width=12,command=MultiPlay)
 b2.place(relx=0.5,rely=0.467,anchor=CENTER)
 screen = Canvas(root, width=400, height=400, bg='PaleVioletRed2')
 root.mainloop()
def exitloop():
    master.destroy()
def center_window(w,h):
    ws = master.winfo_screenwidth()
    hs = master.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    master.geometry('%dx%d+%d+%d' % (w, h, x, y))     
master = Tk()
master.resizable(False,False)
master.title('TicTacToe')
master.geometry('220x180')
center_window(220,180)
master.configure(background='light gray')
label=Label(master, text='Welcome To TictacToe world!!',bg='light gray')
label.pack()
Play = Button(master,text='START',bg='aquamarine',command=newWindow,height=1,width=8)
Quit = Button(master,text='EXIT',bg='aquamarine',height=1,width=8,command=exitloop)
Play.place(relx=0.5,rely=0.4,anchor=CENTER)
Quit.place(relx=0.5,rely=0.547,anchor=CENTER)
mainloop()