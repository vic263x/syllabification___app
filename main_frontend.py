import tkinter as tk
from tkinter import Label, Button, StringVar, PhotoImage
import IPA_buttons as ipa_b
import MOP_button as mop_b
import SSG_button as ssg_b
import authors as auth_b
import help_button as help_b


class App1:

    def __init__(self, top):
        self.top = top
        top.title("Syllabification app")
        top.geometry("1100x540")
        top.configure(background="#ffcce6")

        # fonts
        font01 = "System 25"
        font02 = "System 12 bold"
        font03 = "System 13 bold"
        font04 = "{Segoe UI} 15"
        font05 = "System 10"
        font06 = "System 13"

        self.Label1 = tk.Label(master=top, text="Syllabification App", background="#ffcce6",
                               font=font01, foreground="#5c5c8a")
        self.Label1.place(relx=0.268, rely=0.02, height=51, width=507)

        self.entry1 = tk.Entry(master=top, textvariable=user_input, background="#f2f2f2", foreground="#735c8a",
                               selectbackground="#ff3399", font=font02)
        self.entry1.place(relx=0.049, rely=0.265, height=36, relwidth=0.320)
        user_input.set('HINT: use the buttons below')
        self.entry2 = tk.Entry(master=top, textvariable=sonority, background="#f2f2f2", foreground="#735c8a",
                               selectbackground="#ff3399", font=font02)
        self.entry2.place(relx=0.635, rely=0.265, height=36, width=137)
        sonority.set('← Step 2')

        # ___Entry Control Buttons___
        self.Button1 = tk.Button(master=top, text='CLEAR', background='#ffe6f2',
                                 font=font06, foreground="#5c5c8a", activebackground="#ffe6f9",
                                 borderwidth='1', cursor="heart", command=lambda: ipa_b.clear_key(user_input, sonority))
        self.Button1.place(relx=0.375, rely=0.265, height=36, width=67)
        self.Button1 = tk.Button(master=top, text='Step1: MOP', background='#ffe6f2',
                                 font=font06, foreground="#5c5c8a", activebackground="#ffe6f9",
                                 borderwidth='1', cursor="heart", command=lambda: ipa_b.done_key(user_input))
        self.Button1.place(relx=0.44, rely=0.265, height=36, width=137)
        self.Button1 = tk.Button(master=top, text='SSG', background='#ffe6f2',
                                 font=font06, foreground="#5c5c8a", activebackground="#ffe6f9",
                                 borderwidth='1', cursor="heart", command=lambda: ipa_b.ssg_key(user_input, sonority))
        self.Button1.place(relx=0.57, rely=0.265, height=36, width=67)

        # ___Main Control Buttons___
        self.Button1 = tk.Button(master=top, text='About MOP', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9",
                                 cursor="heart", command=mop_b.about_MOP)
        self.Button1.place(relx=0.82, rely=0.1, height=53, width=150)
        self.Button1 = tk.Button(master=top, text='About SSG', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9",
                                 cursor="heart", command=ssg_b.about_SSG)
        self.Button1.place(relx=0.82, rely=0.25, height=53, width=150)
        self.Button1 = tk.Button(master=top, text='AUTHORS', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9",
                                 cursor="heart", command=auth_b.authors)
        self.Button1.place(relx=0.82, rely=0.4, height=53, width=150)

        image = tk.PhotoImage(file="contact.png")
        l1 = tk.Label(top, image=image, borderwidth=0)
        l1.image = image
        l1.pack()
        l1.place(relx=0.835, rely=0.53)

        self.Label1 = tk.Label(master=top, text="Send us your feedback!", background="#ffcce6",
                               font=font05, foreground="#5c5c8a")
        self.Label1.place(relx=0.775, rely=0.71, height=20, width=250)
 
        self.Button1 = tk.Button(master=top, text='EXIT', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9", 
                                 cursor="heart", command=close_window)
        self.Button1.place(relx=0.82, rely=0.795, height=53, width=150)


        # ___IPA Buttons___
        # 1st row
        self.Label2 = tk.Label(master=top, 
                                text="-----VOWELS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------", 
                                background="#ffcce6", font=font05, foreground="#c5abed")
        self.Label2.place(relx=0.045, rely=0.38, height=20, width=800)
        self.Button2 = tk.Button(master=top, text='''i''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('i', user_input))
        self.Button2.place(relx=0.05, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ɪ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ɪ', user_input))
        self.Button2.place(relx=0.115, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''e''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('e', user_input))
        self.Button2.place(relx=0.18, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''æ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1', 
                                 command=lambda: ipa_b.ipa_key('æ', user_input))
        self.Button2.place(relx=0.245, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ə''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ə', user_input))
        self.Button2.place(relx=0.31, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ʌ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ʌ', user_input))
        self.Button2.place(relx=0.375, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ɚ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ɚ', user_input))
        self.Button2.place(relx=0.44, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''u''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('u', user_input))
        self.Button2.place(relx=0.505, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ɔ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ɔ', user_input))
        self.Button2.place(relx=0.57, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ʊ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ʊ', user_input))
        self.Button2.place(relx=0.635, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ɑ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ɑ', user_input))
        self.Button2.place(relx=0.7, rely=0.42, height=44, width=67)
        # 2nd row
        self.Label2 = tk.Label(master=top, 
                                text="  ----PLOSIVES----------------------------------------------------------------------------------------------------                      -----NASALS--------------------------------   ", 
                                background="#ffcce6", font=font05, foreground="#c5abed")
        self.Label2.place(relx=0.045, rely=0.51, height=20, width=800)
        self.Button2 = tk.Button(master=top, text='''p''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('p', user_input))
        self.Button2.place(relx=0.05, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''b''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('b', user_input))
        self.Button2.place(relx=0.115, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''t''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('t', user_input))
        self.Button2.place(relx=0.18, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''d''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('d', user_input))
        self.Button2.place(relx=0.245, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''k''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('k', user_input))
        self.Button2.place(relx=0.31, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''g''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('g', user_input))
        self.Button2.place(relx=0.375, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ʔ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ʔ', user_input))
        self.Button2.place(relx=0.44, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''m''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('m', user_input))
        self.Button2.place(relx=0.57, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''n''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('n', user_input))
        self.Button2.place(relx=0.635, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ŋ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ŋ', user_input))
        self.Button2.place(relx=0.7, rely=0.55, height=44, width=67)
        # 3rd row
        self.Label2 = tk.Label(master=top, 
                                text="   ----FRICATIVES---------------------------------------------------------------------------------------------------------------------------------------                     TAP/FLAP     ", 
                                background="#ffcce6", font=font05, foreground="#c5abed")
        self.Label2.place(relx=0.045, rely=0.64, height=20, width=800)
        self.Button2 = tk.Button(master=top, text='''f''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('f', user_input))
        self.Button2.place(relx=0.05, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''v''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('v', user_input))
        self.Button2.place(relx=0.115, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''θ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('θ', user_input))
        self.Button2.place(relx=0.18, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ð''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ð', user_input))
        self.Button2.place(relx=0.245, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''s''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('s', user_input))
        self.Button2.place(relx=0.31, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''z''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('z', user_input))
        self.Button2.place(relx=0.375, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ʃ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ʃ', user_input))
        self.Button2.place(relx=0.44, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ʒ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ʒ', user_input))
        self.Button2.place(relx=0.505, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''h''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('h', user_input))
        self.Button2.place(relx=0.57, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ɾ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ɾ', user_input))
        self.Button2.place(relx=0.7, rely=0.68, height=44, widt=67)

        # 4th row
        self.Label2 = tk.Label(master=top, 
                                text=" ---AFFRICATES---------                       -----LIQUIDS-------------                    -----GLIDES-------------- ", 
                                background="#ffcce6", font=font05, foreground="#c5abed")
        self.Label2.place(relx=0.05, rely=0.77, height=20, width=560)
        self.Button2 = tk.Button(master=top, text='''ʧ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ʧ', user_input))
        self.Button2.place(relx=0.05, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ʤ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('ʤ', user_input))
        self.Button2.place(relx=0.115, rely=0.81, height=44, width=67)

        self.Button2 = tk.Button(master=top, text='''r''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('r', user_input))
        self.Button2.place(relx=0.245, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''l''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('l', user_input))
        self.Button2.place(relx=0.31, rely=0.81, height=44, width=67)

        self.Button2 = tk.Button(master=top, text='''w''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('w', user_input))
        self.Button2.place(relx=0.44, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''j''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 command=lambda: ipa_b.ipa_key('j', user_input))
        self.Button2.place(relx=0.505, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''HELP ME PLS''', background="#ffe6f2", font=font03,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1',
                                 cursor="heart", command=help_b.about_help)
        self.Button2.place(relx=0.635, rely=0.81, height=44, width=138)


def close_window():
    root.destroy()


root = tk.Tk()

user_input = tk.StringVar()
sonority = tk.StringVar()

my_gui = App1(root)
root.mainloop()
