
import tkinter as tk
from tkinter import Label, StringVar, Scrollbar


def about_help():
    about = tk.Tk()
    about.title("Help me pls")
    about.resizable(width='false', height='true')
    about.configure(background="#ffcce6")


    S = tk.Scrollbar(about)
    T = tk.Text(about, height=10, width=35, 
                font="{Segoe UI} 14 bold", foreground="#5c5c8a", background="#ffcce6")
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """ This is the SYLLABIFICATION APP.
       To use it you have to enter the word
       of your choice into the left textbox 
       and click on the MOP button. 
 REMEMBER to use our IPA keyboard! 
       If you want to check whether MOP 
       syllabification of your word is 
       well-formed in terms of sonority,
       click on the SSG button.
 BEFORE CHECKING SONORITY,
       you have to go through stage 1:
       MOP syllabification.
       
       ENJOY!
                             -Victoria & Martha""" 
    

    
    T.insert(tk.END, quote)
    tk.mainloop()