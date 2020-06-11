import tkinter as tk
from tkinter import Label, StringVar, Scrollbar


def about_MOP():
    about = tk.Tk()
    about.title("What's the MOP?")
    about.configure(background="#ffcce6")
    about.resizable(width='false', height='true')

    S = tk.Scrollbar(about)
    T = tk.Text(about, height=10, width=35, 
                font="{Segoe UI} 19 bold", foreground="#5c5c8a", background="#ffcce6")
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """ Maximal Onset Principle 
            is a principle determining 
            underlying syllable division. 
            It states that intervocalic 
            consonants are maximally 
            assigned to the onsets of 
            syllables in conformity with
            universal and language-specific 
            conditions."""
    T.insert(tk.END, quote)
    tk.mainloop()



