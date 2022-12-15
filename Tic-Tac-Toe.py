#TIC-TAC-TOE

import tkinter as gui
from tkinter import messagebox;


app=gui.Tk()
app.geometry('590x320')
app.title('Tic-Tac-Toe')

turn=gui.Label(app,text='0')
#turn.place(x=50,y=300)

def reset():
    strt.configure(text='Play Again',state=gui.NORMAL)
    b1.configure(text='')
    b2.configure(text='')
    b3.configure(text='')
    b4.configure(text='')
    b5.configure(text='')
    b6.configure(text='')
    b7.configure(text='')
    b8.configure(text='')
    b9.configure(text='')

def winmsg():
    if int(turn.cget('text'))%2==0:
        player='One'
    else:
        player='Two'
    m=gui.messagebox.showinfo(title='Tic-Tac-Toe',
                              message='Player {} wins!'.format(player))
    reset()
    

def check():
    
    if b1.cget('text')==b5.cget('text')==b9.cget('text')!='':
        winmsg()
    elif b3.cget('text')==b5.cget('text')==b7.cget('text')!='':
        winmsg()
    elif b1.cget('text')==b2.cget('text')==b3.cget('text')!='':
        winmsg()
    elif b4.cget('text')==b5.cget('text')==b6.cget('text')!='':
        winmsg()
    elif b7.cget('text')==b8.cget('text')==b9.cget('text')!='':
        winmsg()
    elif b1.cget('text')==b4.cget('text')==b7.cget('text')!='':
        winmsg()
    elif b2.cget('text')==b5.cget('text')==b8.cget('text')!='':
        winmsg()
    elif b3.cget('text')==b6.cget('text')==b9.cget('text')!='':
        winmsg()
    elif b1.cget('text')!='' and b2.cget('text')!='' and \
        b3.cget('text')!='' and b4.cget('text')!='' and \
        b5.cget('text')!='' and b6.cget('text')!='' and\
        b7.cget('text')!='' and b8.cget('text')!='' \
        and b9.cget('text')!='':
        m=gui.messagebox.showinfo(title='Tic-Tac-Toe',
                              message="It's a Tie")
        reset()
    else:
        pass

def start():
    turnlbl.configure(text='Player One')
    strt.configure(state=gui.DISABLED)
    turn.configure(text=str(int(turn.cget('text'))+1))
    b1.configure(state=gui.NORMAL)
    b2.configure(state=gui.NORMAL)
    b3.configure(state=gui.NORMAL)
    b4.configure(state=gui.NORMAL)
    b5.configure(state=gui.NORMAL)
    b6.configure(state=gui.NORMAL)
    b7.configure(state=gui.NORMAL)
    b8.configure(state=gui.NORMAL)
    b9.configure(state=gui.NORMAL)
    
def b1_clk():
    if int(turn.cget('text'))%2==0:
        b1.configure(text='O')
        turnlbl.configure(text='Player One')
    else:
        b1.configure(text='X')
        turnlbl.configure(text='Player Two')
    b1['state']=gui.DISABLED
    turn.configure(text=str(int(turn.cget('text'))+1))
    check()    
    
def b2_clk():
    if int(turn.cget('text'))%2==0:
        b2.configure(text='O')
        turnlbl.configure(text='Player One')
    else:
        b2.configure(text='X')
        turnlbl.configure(text='Player Two')
    b2['state']=gui.DISABLED
    turn.configure(text=str(int(turn.cget('text'))+1))  
    check()

def b3_clk():
    if int(turn.cget('text'))%2==0:
        b3.configure(text='O')
        turnlbl.configure(text='Player One')
    else:
        b3.configure(text='X')
        turnlbl.configure(text='Player Two')
    b3['state']=gui.DISABLED
    turn.configure(text=str(int(turn.cget('text'))+1)) 
    check()

def b4_clk():
    if int(turn.cget('text'))%2==0:
        b4.configure(text='O')
        turnlbl.configure(text='Player One')
    else:
        b4.configure(text='X')
        turnlbl.configure(text='Player Two')
    b4['state']=gui.DISABLED
    turn.configure(text=str(int(turn.cget('text'))+1))
    check()

def b5_clk():
    if int(turn.cget('text'))%2==0:
        b5.configure(text='O')
        turnlbl.configure(text='Player One')
    else:
        b5.configure(text='X')
        turnlbl.configure(text='Player Two')
    b5['state']=gui.DISABLED
    turn.configure(text=str(int(turn.cget('text'))+1)) 
    check()

def b6_clk():
    if int(turn.cget('text'))%2==0:
        b6.configure(text='O')
        turnlbl.configure(text='Player One')
    else:
        b6.configure(text='X')
        turnlbl.configure(text='Player Two')
    b6['state']=gui.DISABLED
    turn.configure(text=str(int(turn.cget('text'))+1)) 
    check()

def b7_clk():
    if int(turn.cget('text'))%2==0:
        b7.configure(text='O')
        turnlbl.configure(text='Player One')
    else:
        b7.configure(text='X')
        turnlbl.configure(text='Player Two')
    b7['state']=gui.DISABLED
    turn.configure(text=str(int(turn.cget('text'))+1))
    check()

def b8_clk():
    if int(turn.cget('text'))%2==0:
        b8.configure(text='O')
        turnlbl.configure(text='Player One')
    else:
        b8.configure(text='X')
        turnlbl.configure(text='Player Two')
    b8['state']=gui.DISABLED
    turn.configure(text=str(int(turn.cget('text'))+1)) 
    check()

def b9_clk():
    if int(turn.cget('text'))%2==0:
        b9.configure(text='O')
        turnlbl.configure(text='Player One')
    else:
        b9.configure(text='X')
        turnlbl.configure(text='Player Two')
    b9['state']=gui.DISABLED
    turn.configure(text=str(int(turn.cget('text'))+1)) 
    check()
    

lbl1=gui.Label(app,text='Turn : ',font=('',18))
turnlbl=gui.Label(app,text='',font=('',18))
lbl1.place(x=350,y=50)
turnlbl.place(x=440,y=50)

strt=gui.Button(app,width=7,height=1,text='START',font=('',18),
                command=start)
strt.place(x=350,y=190)

b1=gui.Button(app,width=3,height=1,text='',font=('',20),
              state=gui.DISABLED,command=b1_clk)
b2=gui.Button(app,width=3,height=1,text='',font=('',20),
              state=gui.DISABLED,command=b2_clk)
b3=gui.Button(app,width=3,height=1,text='',font=('',20),
              state=gui.DISABLED,command=b3_clk)
b4=gui.Button(app,width=3,height=1,text='',font=('',20),
              state=gui.DISABLED,command=b4_clk)
b5=gui.Button(app,width=3,height=1,text='',font=('',20),
              state=gui.DISABLED,command=b5_clk)
b6=gui.Button(app,width=3,height=1,text='',font=('',20),
              state=gui.DISABLED,command=b6_clk)
b7=gui.Button(app,width=3,height=1,text='',font=('',20),
              state=gui.DISABLED,command=b7_clk)
b8=gui.Button(app,width=3,height=1,text='',font=('',20),
              state=gui.DISABLED,command=b8_clk)
b9=gui.Button(app,width=3,height=1,text='',font=('',20),
              state=gui.DISABLED,command=b9_clk)

b1.place(x=50,y=50)
b2.place(x=120,y=50)
b3.place(x=190,y=50)
b4.place(x=50,y=120)
b5.place(x=120,y=120)
b6.place(x=190,y=120)
b7.place(x=50,y=190)
b8.place(x=120,y=190)
b9.place(x=190,y=190)

app.mainloop()