from tkinter import *
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
import csdl
from tkinter import messagebox
import dangnhap
import socket
import mysql.connector
import pickle
import cv2
import face_recognition
import them_sv_moi
import diemdanhsv
import thongke
import diemdanhbu


def main():


    win=Tk()
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Menu tkinter")
    img_bg=ImageTk.PhotoImage(file="img/bg_lop.png")
    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    makhoa=csdl.makhoa_tu_email(email)
    

#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    

 
    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    
    
    win.mainloop()

