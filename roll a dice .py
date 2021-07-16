from tkinter import *
from random import randint
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='# of Die Sides')
        self.lbl2=Label(win, text='Roll Result')
        self.lbl3=Label(win, text='Dice Rolling Simulator', font=("Helvetica", 20))
        self.t1=Entry()
        self.t2=Entry()
        self.btn1 = Button(win, text='Roll Dice')
        self.lbl1.place(x=100, y=100)
        self.t1.place(x=200, y=100)
        self.b1=Button(win, text='Roll Dice', font=("Helvetica", 16), command=self.roll)
        self.b1.place(x=200, y=140)
        self.b1.config(height=1, width=8)
        self.lbl2.place(x=100, y=200)
        self.t2.place(x=200, y=200)
        self.lbl3.place(x=100, y=35)
    def roll(self):
        self.t2.delete(0, 'end')
        n=int(self.t1.get())
        result=randint(1,n)
        self.t2.insert(END, str(result))
window=Tk()
mywin=MyWindow(window)
window.title('Dice Roller')
window.geometry("400x300+10+10")
window.mainloop()