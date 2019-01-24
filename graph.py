from tkinter import *
import sqlite3
import pyttsx3
conn = sqlite3.connect('adv.db')
c = conn.cursor()
from tkinter import messagebox
root = Tk()
def speak():
    words = 150
    ide = entry.get()
    engine = pyttsx3.init()
    mytext = StringVar()
    rate = engine.setProperty('rate',words)
    mytext = 'Hi  i am John','I am going to explain about this graph which was created by',c.execute('select name from signup where id = ?',(ide,)).fetchone()[0],'which has x range and y range of',c.execute('select xrange from coordinate where id = ?',(ide,)).fetchone()[0],'and',c.execute('select xrange from coordinate where id = ?',(ide,)).fetchone()[0],'First it goes to',c.execute('select x1 from coordinate where id = ?',(ide,)).fetchone()[0],'coma',c.execute('select y1 from coordinate where id = ?',(ide,)).fetchone()[0],'and then it goes to',c.execute('select x2 from coordinate where id = ?',(ide,)).fetchone()[0],'coma',c.execute('select y2 from coordinate where id = ?',(ide,)).fetchone()[0],'from there it goes to',c.execute('select x3 from coordinate where id = ?',(ide,)).fetchone()[0],'coma',c.execute('select y3 from coordinate where id = ?',(ide,)).fetchone()[0],'and to',c.execute('select x4 from coordinate where id = ?',(ide,)).fetchone()[0],'coma',c.execute('select y4 from coordinate where id = ?',(ide,)).fetchone()[0],'finally it reaches',c.execute('select x5 from coordinate where id = ?',(ide,)).fetchone()[0],'coma',c.execute('select y5 from coordinate where id = ?',(ide,)).fetchone()[0],'Thank You'
    engine.say(mytext)
    engine.runAndWait()
def call(aa,a,bb,value,value1,value2,value3,value4,value5,value6,value7,value8,value9):
    te = aa
    q = 1
    r = 1
    ff = aa / (bb - 1)
    rr = a / (bb - 1)
    t = rr
    if (bb > 0 and bb < 21):
        cc = 25
    ans = (cc * (bb - 1)) / a
    ans1 = (cc * (bb - 1)) / aa
    ans2 = (cc * (bb - 1)) / a
    ans3 = (cc * (bb - 1)) / aa
    ans4 = (cc * (bb - 1)) / a
    ans5 = (cc * (bb - 1)) / aa
    ans6 = (cc * (bb - 1)) / a
    ans7 = (cc * (bb - 1)) / aa
    ans8 = (cc * (bb - 1)) / a
    ans9 = (cc * (bb - 1)) / aa
    canvas = Canvas(root, width=800, height=700)
    canvas.pack()
    blackline = canvas.create_line(80, 50, 80, cc * (bb + 1) + 20)
    blackline1 = canvas.create_line(80, cc * bb + 45, cc * (bb + 1) + 50, cc * bb + 45)
    blackline2 = canvas.create_line(80, 50, 70, 60)
    blackline3 = canvas.create_line(80, 50, 90, 60)
    blackline4 = canvas.create_line(cc * bb + 75, cc * bb + 45, cc * bb + 65, cc * bb + 45 - 10)
    blackline5 = canvas.create_line(cc * bb + 75, cc * bb + 45, cc * bb + 65, cc * bb + 45 + 10)
    dd = 0
    for x in range(0, bb):
        blackline = canvas.create_line(70, 70 + dd, 80, 70 + dd)
        if (x != bb - 1):
            text = canvas.create_text(40, 70 + dd, anchor=W, font="Purisa", text=round(te))
            te = aa - (ff * q)
            q = q + 1
        else:
            text = canvas.create_text(50, 70 + dd, anchor=W, font="Purisa", text="0")
        dd = dd + cc
    dd = 0
    for x in range(0, bb):
        blackline = canvas.create_line(80 + dd, bb * cc + 45, 80 + dd, bb * cc + 55)
        if (x == 0):
            text = canvas.create_text(65 + dd, bb * cc + 65, anchor=W, font="Purisa", text="0")
        else:
            text = canvas.create_text(65 + dd, bb * cc + 65, anchor=W, font="Purisa", text=round(t))
            t = t + rr
        dd = dd + cc
    blackline = canvas.create_line((ans * value) + 80, ((cc * bb) + 45) - (value1 * ans1), ((ans * value) + 80) + 1,
                                   ((cc * bb) + 45) - (value1 * ans1) + 2)
    blackline = canvas.create_line((ans2 * value2) + 80, ((cc * bb) + 45) - (value3 * ans3), ((ans2 * value2) + 80) + 1,
                                   ((cc * bb) + 45) - (value3 * ans3) + 2)
    blackline = canvas.create_line((ans4 * value4) + 80, ((cc * bb) + 45) - (value5 * ans5), ((ans4 * value4) + 80) + 1,
                                   ((cc * bb) + 45) - (value5 * ans5) + 2)
    blackline = canvas.create_line((ans6 * value6) + 80, ((cc * bb) + 45) - (value7 * ans7), ((ans6 * value6) + 80) + 1,
                                   ((cc * bb) + 45) - (value7 * ans7) + 2)
    blackline = canvas.create_line((ans8 * value8) + 80, ((cc * bb) + 45) - (value9 * ans9), ((ans8 * value8) + 80) + 1,
                                   ((cc * bb) + 45) - (value9 * ans9) + 2)
    # coordinate point marking in graph
    var1 = (ans * value) + 80
    var2 = ((cc * bb) + 45) - (value1 * ans1)
    var3 = (ans2 * value2) + 80
    var4 = ((cc * bb) + 45) - (value3 * ans3)
    var5 = (ans4 * value4) + 80
    var6 = ((cc * bb) + 45) - (value5 * ans5)
    var7 = (ans6 * value6) + 80
    var8 = ((cc * bb) + 45) - (value7 * ans7)
    var9 = (ans8 * value8) + 80
    var10 = ((cc * bb) + 45) - (value9 * ans9)
    blackline = canvas.create_line(var1, var2, var3, var4)
    blackline = canvas.create_line(var3, var4, var5, var6)
    blackline = canvas.create_line(var5, var6, var7, var8)
    blackline = canvas.create_line(var7, var8, var9, var10)
def generate():
    conn = sqlite3.connect('adv.db')
    ref = entryv.get()
    c = conn.cursor()
    id1 = entry.get()
    paws = entry1.get()
    password = c.execute('SELECT password FROM signup WHERE id = ? ', (id1,))
    pass1 = password.fetchone()[0]
    if (paws == pass1):
        aaa = c.execute('SELECT yrange FROM coordinate WHERE graph = ? ', (ref,))
        aa = aaa.fetchone()[0]
        aaaa = c.execute('SELECT xrange FROM coordinate WHERE graph = ? ', (ref,))
        a = aaaa.fetchone()[0]
        bbb = c.execute('SELECT div FROM coordinate WHERE graph = ? ', (ref,))
        bb = bbb.fetchone()[0]
        vallu = c.execute('SELECT x1 FROM coordinate WHERE graph = ? ', (ref,))
        value = vallu.fetchone()[0]
        yt = c.execute('SELECT y1 FROM coordinate WHERE graph = ? ', (ref,))
        value1 = yt.fetchone()[0]
        ty = c.execute('SELECT x2 FROM coordinate WHERE graph = ? ', (ref,))
        value2 = ty.fetchone()[0]
        qw = c.execute('SELECT y2 FROM coordinate WHERE graph = ? ', (ref,))
        value3 = qw.fetchone()[0]
        ii = c.execute('SELECT x3 FROM coordinate WHERE graph = ? ', (ref,))
        value4 = ii.fetchone()[0]
        jj = c.execute('SELECT y3 FROM coordinate WHERE graph = ? ', (ref,))
        value5 = jj.fetchone()[0]
        hh = c.execute('SELECT x4 FROM coordinate WHERE graph = ? ', (ref,))
        value6 = hh.fetchone()[0]
        sd = c.execute('SELECT y4 FROM coordinate WHERE graph = ? ', (ref,))
        value7 = sd.fetchone()[0]
        ds = c.execute('SELECT x5 FROM coordinate WHERE graph = ? ', (ref,))
        value8 = ds.fetchone()[0]
        bv = c.execute('SELECT y5 FROM coordinate WHERE graph = ? ', (ref,))
        value9 = bv.fetchone()[0]

        call(aa, a, bb, value, value1, value2, value3, value4, value5, value6, value7, value8, value9)

    else:
        messagebox.showinfo("Message", "Invalid, try after sometime ")
        root.destroy()

label = Label(root,text="Enter id").pack()
entry = Entry(root)
entry.pack()
label = Label(root,text="Enter Password").pack()
entry1 = Entry(root)
entry1.pack()
entry1.config(show="#")
label = Label(root,text="Enter graph Id").pack()
entryv = Entry(root)
entryv.pack()
w = Button(root,text="Generate graph",command=generate).pack()
we = Button(root,text="Explain",command=speak).pack()
root.mainloop()
