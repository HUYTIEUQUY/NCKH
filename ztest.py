from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os

def showimg():
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All file","*.*")))
    img=Image.open(fln)
    img.thumbnail((150,150))
    img=ImageTk.PhotoImage(img)
    lb.config(image=img)
    lb.image=img

win = Tk()
win.title("cHỌN ẢNH")
win.geometry("500x500")

fg=Frame(win)
fg.pack(side=BOTTOM,padx=15,pady=15)

lb=Label(win)
lb.pack()

btn = Button(fg,text="Browse Image",command=showimg)
btn.pack(side=LEFT )

win.mainloop()