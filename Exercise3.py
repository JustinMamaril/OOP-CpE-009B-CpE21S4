from tkinter import *
class MyWindow:
    def __init__(self,win):
        #common widgets
        win.configure(bg = "#D3AC8B")
        self.Label1 = Label(win,text = "Calculator", fg="#966443",bg = "#D3AC8B" ,font = ("Arial Narrow", 30, "bold"))
        self.Label1.place(x=125, y=25)


        self.Label2 = Label(win,text = "Number 1:", fg = "White",bg = "#D3AC8B", font = ("Arial Narrow", 15))
        self.Label2.place(x=60, y=100)
        self.Entry1 = Entry(win, bd=2)
        self.Entry1.place(x=150, y=105)

        self.Label3 = Label(win,text = "Number 2:", fg = "White",bg = "#D3AC8B", font = ("Arial Narrow", 15))
        self.Label3.place(x=60, y=160)
        self.Entry2 = Entry(win, bd=2)
        self.Entry2.place(x=150, y=165)

        self.Label4 = Label(win,text = "Result:", fg = "White",bg = "#D3AC8B", font = ("Arial Narrow", 15))
        self.Label4.place(x=60, y=220)
        self.Entry3 = Entry(win, bd=2)
        self.Entry3.place(x=150, y=225)

        self.Button1 = Button(win, text = "Add", width= 6, height = 2, command = self.add)
        self.Button1.place(x= 60, y=290)

        self.Button2 = Button(win, text="Sub", width=6, height=2, command = self.sub)
        self.Button2.place(x=140, y=290)

        self.Button3 = Button(win, text="Multi", width=6, height=2, command = self.multi)
        self.Button3.place(x=220, y=290)

        self.Button4 = Button(win, text="Div", width=6, height=2, command = self.div)
        self.Button4.place(x=300, y=290)

    def add(self):
        self.Entry3.delete(0,'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def multi(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))


window = Tk()
MyWin=MyWindow(window)


window.geometry("400x400+10+10")
window.title("Standard Calculator")
window.mainloop()