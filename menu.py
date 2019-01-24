from tkinter import *
root = Tk()
def close_window ():
    root.destroy()
def view():
    import View.py
def loginn():
    import Login.py
def gui():
    import gui.py
def graph():
    import graph.py
label = Label( root,text="MENU",font=("Helvetica", 16))
label.grid(row=0,column=0)
label = Label( root,text="",font=("Helvetica", 16))
label.grid(row=1,column=0)
w=Button(root,text='SIGNUP',command=loginn)
w.grid(row=2,column=0)
w=Button(root,text='VIEW VALUES',command=view)
w.grid(row=2,column=1)
w=Button(root,text='SAVE VALUES',command=gui)
w.grid(row=2,column=2)
w=Button(root,text='GENERATE GRAPH',command=graph)
w.grid(row=2,column=3)
w=Button(root,text='QUIT',command=close_window)
w.grid(row=2,column=4)
root.mainloop()