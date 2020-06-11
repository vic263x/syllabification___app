import tkinter as tk
from tkinter import Label, StringVar, Scrollbar


def about_SSG():
    about = tk.Tk()
    about.title("What's the SSG?")
    about.configure(background="#ffcce6")
    about.resizable(width='false', height='true')


    S = tk.Scrollbar(about)
    T = tk.Text(about, height=10, width=35, 
                font="{Segoe UI} 19 bold", foreground="#5c5c8a", background="#ffcce6")
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """ Sonority Sequencing Generalization: 
            universal phonological principle
            refering to the syllable structure,
            which says that the sonority
            should rise from the onset
            to the nucleus (the peak)
            and the decrease to the coda."""
    T.insert(tk.END, quote)
    tk.mainloop()
