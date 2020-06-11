import tkinter as tk
from tkinter import Label, Button, PhotoImage, Frame
import webbrowser


def authors():
    about = tk.Toplevel()
    about.geometry("313x290")
    about.title("AUTHORS")
    about.resizable(width='false', height='false')
    about.configure(background="#ffcce6")

    new = 1
    url1 = "https://github.com/vic263x"
    def openweb_vi():
        webbrowser.open(url1,new=new)
    url2 = "https://github.com/FlyingMedusa"
    def openweb_ma():
        webbrowser.open(url2,new=new)

    frame0 = tk.Frame(about, borderwidth=0)
    frame0.grid(row=0, column=0, columnspan=2)
    frame1 = tk.Frame(about, borderwidth=0)
    frame1.grid(row=1, column=0)
    frame2 = tk.Frame(about, borderwidth=0)
    frame2.grid(row=1, column=1)
    frame3 = tk.Frame(about, borderwidth=0)
    frame3.grid(row=2, column=0)
    frame4 = tk.Frame(about, borderwidth=0)
    frame4.grid(row=2, column=1)
    frame5 = tk.Frame(about, borderwidth=0)
    frame5.grid(row=3, column=0, columnspan=2)
    frame6 = tk.Frame(about, borderwidth=0)
    frame6.grid(row=4, column=0, columnspan=2)

    labelinfo = Label(frame0, text="Authors", foreground="#5c5c8a", font="System 19 bold", 
    background="#ffcce6")
    labelinfo.pack()

    #___Buttons___
    photo1 = tk.PhotoImage(file="Vi.PNG")
    button1 = tk.Button(frame1, compound=tk.TOP, width=148, height=148, image=photo1, 
                        bg='white', cursor="heart", command=openweb_vi)
    button1.pack(side=tk.LEFT, padx=2, pady=2)

    photo2 = tk.PhotoImage(file="Ma.PNG")
    button1 = tk.Button(frame2, compound=tk.TOP, width=148, height=148, image=photo2, 
                        bg='white', cursor="heart", command=openweb_ma)
    button1.pack(side=tk.LEFT, padx=2, pady=2)

    #___Labels under images___
    Label1 = tk.Label(frame3, text="Wiktoria Połetek", background="#ffcce6",
                               font="System 13", foreground="#505095")
    Label1.pack()
    Label1 = tk.Label(frame4, text="Marta Sleboda", background="#ffcce6",
                               font="System 13", foreground="#505095")
    Label1.pack()
    Label1 = tk.Label(frame5, text="♡", background="#ffcce6",
                               font="System 11", foreground="#5c5c8a")
    Label1.pack()
    Label1 = tk.Label(frame6, text="↑Click on ponies to go to our github accounts↑  ", background="#ffcce6",
                               font="System 11", foreground="#5c5c8a")
    Label1.pack()

    about.mainloop()

