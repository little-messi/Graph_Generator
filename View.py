from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
conn = sqlite3.connect('adv.db')
c = conn.cursor()
def texty():
    conn = sqlite3.connect('adv.db')
    c = conn.cursor()
    passw = entry1.get()
    datab = c.execute('select password from signup where id = ?', (entry.get(),)).fetchone()[0]
    if(entry1.get()==datab):
        lab11 = Label(root,text="Graph No").grid(row=4,column=3)
        lab11 = Label(root, text="X-RANGE").grid(row=4, column=4)
        lab11 = Label(root, text="Y-RANGE").grid(row=4, column=5)
        lab11 = Label(root, text="DIV").grid(row=4, column=6)
        lab11 = Label(root, text="X1").grid(row=4, column=7)
        lab11 = Label(root, text="Y1").grid(row=4, column=8)
        lab11 = Label(root, text="X2").grid(row=4, column=9)
        lab11 = Label(root, text="Y2").grid(row=4, column=10)
        lab11 = Label(root, text="X3").grid(row=4, column=11)
        lab11 = Label(root, text="Y3").grid(row=4, column=12)
        lab11 = Label(root, text="X4").grid(row=4, column=13)
        lab11 = Label(root, text="Y4").grid(row=4, column=14)
        lab11 = Label(root, text="X5").grid(row=4, column=15)
        lab11 = Label(root, text="Y5").grid(row=4, column=16)
        roww = c.execute("select graph from coordinate where id = ?", (entry.get(),)).fetchall()
        roww1 = c.execute("select xrange from coordinate where id = ?", (entry.get(),)).fetchall()
        roww2 = c.execute("select yrange from coordinate where id = ?", (entry.get(),)).fetchall()
        roww3 = c.execute("select div from coordinate where id = ?", (entry.get(),)).fetchall()
        roww4 = c.execute("select x1 from coordinate where id = ?", (entry.get(),)).fetchall()
        roww5 = c.execute("select y1 from coordinate where id = ?", (entry.get(),)).fetchall()
        roww6 = c.execute("select x2 from coordinate where id = ?", (entry.get(),)).fetchall()
        roww7 = c.execute("select y2 from coordinate where id = ?", (entry.get(),)).fetchall()
        roww8 = c.execute("select x3 from coordinate where id = ?", (entry.get(),)).fetchall()
        roww9 = c.execute("select y3 from coordinate where id = ?", (entry.get(),)).fetchall()
        roww10 = c.execute("select x4 from coordinate where id = ?", (entry.get(),)).fetchall()
        roww11 = c.execute("select y4 from coordinate where id = ?", (entry.get(),)).fetchall()
        roww12 = c.execute("select x5 from coordinate where id = ?", (entry.get(),)).fetchall()
        roww13 = c.execute("select y5 from coordinate where id = ?", (entry.get(),)).fetchall()
        length = len(roww)
        n=5
        x=0
        while x < length:
            yt = Label(root,text=roww[x]).grid(row=n,column=3)
            yt = Label(root, text=roww1[x]).grid(row=n, column=4)
            yt = Label(root, text=roww2[x]).grid(row=n, column=5)
            yt = Label(root, text=roww3[x]).grid(row=n, column=6)
            yt = Label(root, text=roww4[x]).grid(row=n, column=7)
            yt = Label(root, text=roww5[x]).grid(row=n, column=8)
            yt = Label(root, text=roww6[x]).grid(row=n, column=9)
            yt = Label(root, text=roww7[x]).grid(row=n, column=10)
            yt = Label(root, text=roww8[x]).grid(row=n, column=11)
            yt = Label(root, text=roww9[x]).grid(row=n, column=12)
            yt = Label(root, text=roww10[x]).grid(row=n, column=13)
            yt = Label(root, text=roww11[x]).grid(row=n, column=14)
            yt = Label(root, text=roww12[x]).grid(row=n, column=15)
            yt = Label(root, text=roww13[x]).grid(row=n, column=16)
            n=n+1
            x=x+1
    else:
        messagebox.showinfo("Error", "Invalid Info")
        root.destroy()


lab = Label(root,text="enter id").grid(row=1,column=1)
entry = Entry(root)
entry.grid(row=1,column=2)
entry1 = Entry(root)
entry1.grid(row=2,column=2)
lab1 = Label(root,text="enter password").grid(row=2,column=1)
w = Button(root,text="View",command=texty).grid(row=3,column=1)
w1 = Button(root,text="Quit",command=root.destroy).grid(row=3,column=2)
root.mainloop()