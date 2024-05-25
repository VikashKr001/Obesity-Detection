
from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
#from pymsgbox import *


root=tk.Tk()

root.title("Obesity Classification Using Machine Learning")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

image2 =Image.open('b4.jpg')
image2 =image2.resize((w,h))

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="Obesity Classification", font=('times', 35,' bold '), height=1, width=65,bg="#560319",fg="white")
w.place(x=0, y=10)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="black")


from tkinter import messagebox as ms


def call_file():
    from subprocess import call
    call(['python','Check.py'])
    #import Check.py
    #Check.py()


def window1():
    root.destroy()
    

def window():
    from subprocess import call
    call(['python','GUI_Master.py'])




framed1 = tk.LabelFrame(root, text=" -", width=250, height=360, bd=5, font=('times', 14, ' bold '),bg="black",fg="white")
framed1.grid(row=0, column=0, sticky='nw')
framed1.place(x=170, y=200)


exit1 = tk.Button(root, text="Prediction", command=call_file, width=15, height=2, font=('times', 15, ' bold '),bg="#560319",fg="white")
exit1.place(x=200, y=230)

exit2 = tk.Button(root, text="Exit", command=window1, width=15, height=2, font=('times', 15, ' bold '),bg="Red",fg="white")
exit2.place(x=200, y=430)

exit2 = tk.Button(root, text="Detection", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="#560319",fg="white")
exit2.place(x=200, y=330)


root.mainloop()
