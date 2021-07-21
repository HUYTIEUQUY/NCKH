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
import admin_lop
import admin_thongke
import admin_tkb



def main():
    def menuthongke():
        win.destroy()
        admin_thongke.main()
    def menutkb():
        win.destroy()
        admin_tkb.main()
    def menulop():
        win.destroy()
        admin_lop.main()
    def menudangxuat():
        ten_thiet_bi = socket.gethostname()
        file=open(ten_thiet_bi+".txt","w")
        file.write("")
        file.close()
        win.destroy()
        dangnhap.main()

    win=Tk()
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Menu tkinter")
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_lop.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_admin/btn_dangxuat.png")
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien1.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke.png")
    img_btnthem=ImageTk.PhotoImage(file="img_admin/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_admin/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_admin/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")

    
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

    menudangxuat=Button(bg,image=img_menudangxuat,bd=0,highlightthickness=0,command=menudangxuat)
    menudangxuat.place(x=248,y=44)
    menulophoc=Button(bg,image=img_menulophoc,bd=0,highlightthickness=0,command=menulop)
    menulophoc.place(x=43,y=127)
    menugiangvien=Button(bg,image=img_menugiangvien,bd=0,highlightthickness=0,command=main)
    menugiangvien.place(x=43,y=245)
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0,command=menutkb)
    menutkb.place(x=43,y=363)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=43,y=481)

    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0)
    btnthem.place(x=487,y=181)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0)
    btnsua.place(x=637,y=181)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0)
    btnxoa.place(x=770,y=181)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0)
    btntimkiem.place(x=913,y=250)

 
    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    
    
    win.mainloop()

