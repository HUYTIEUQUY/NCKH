from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
import csdl
import csdl_gv
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
import admin_monhoc



def main():
    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)
    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        data_magv.set(item['values'][1])
        data_ten.set(item['values'][2])
        data_email.set(item['values'][4])
        data_ngaysinh.set(item['values'][3])

    def khoiphuc():
        ndtimkiem.set("")
        row=csdl_gv.banggv(makhoa)
        update(row)
    def timkiem():
        row=csdl_gv.timkiem_gv(makhoa,ndtimkiem.get())
        update(row)
    def them():
        csdl_gv.themgv(makhoa,data_email.get(),data_ngaysinh.get(),data_ten.get())
        data_ten.set("")
        data_email.set("")
        data_ngaysinh.set("")
        khoiphuc()
    def xoa():
        csdl_gv.xoagv(data_magv.get(),data_email.get())
        data_ten.set("")
        data_email.set("")
        data_ngaysinh.set("")
        khoiphuc()
    def sua():
        csdl_gv.suagv(data_magv.get(),data_ten.get(),data_ngaysinh.get())
        data_ten.set("")
        data_email.set("")
        data_ngaysinh.set("")
        khoiphuc()
    def menuthongke():
        win.destroy()
        admin_thongke.main()
    def menumonhoc():
        win.destroy()
        admin_monhoc.main()
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
    def chonngay(cal,btn):
        data_ngaysinh.set(csdl.dinh_dang_ngay(cal.get_date()))
        cal.destroy()
        btn.destroy()
        Label(f).pack()
    def chonlich():
        
        cal = Calendar(f,selectmode="day",year=2021,month=7,day=16,bg="white")
        cal.pack()
        btn=Button(f,image=img_btnchon,bg="white",command=lambda:chonngay(cal,btn))
        btn.pack()

    win=Tk()
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Menu tkinter")
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_giangvien.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_admin/btn_dangxuat.png")
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien1.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke.png")
    img_btnthem=ImageTk.PhotoImage(file="img_admin/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_admin/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_admin/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")
    img_btnchon=ImageTk.PhotoImage(file="img_admin/btn_chon.png")
    img_btnchonlich=ImageTk.PhotoImage(file="img_admin/chonlich.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    makhoa=csdl.makhoa_tu_email(email)
    data_ten=StringVar()
    data_email=StringVar()
    data_ngaysinh=StringVar()
    ndtimkiem=StringVar()
    data_magv=StringVar()

#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menudangxuat=Button(bg,image=img_menudangxuat,bd=0,highlightthickness=0,command=menudangxuat)
    menudangxuat.place(x=248,y=44)
    menulophoc=Button(bg,image=img_menulophoc,bd=0,highlightthickness=0,command=menulop)
    menulophoc.place(x=30,y=128)
    menugiangvien=Button(bg,image=img_menugiangvien,bd=0,highlightthickness=0)
    menugiangvien.place(x=30,y=212)
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0,command=menutkb)
    menutkb.place(x=30,y=296)
    menumonhoc=Button(bg,image=img_menumonhoc,bd=0,highlightthickness=0,command=menumonhoc)
    menumonhoc.place(x=30,y=380)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=30,y=461)

    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command=them)
    btnthem.place(x=487,y=240)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0, command=sua)
    btnsua.place(x=637,y=240)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=240)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,command=timkiem)
    btntimkiem.place(x=881,y=292)
    btnchonlich=Button(bg,image=img_btnchonlich,bd=0,highlightthickness=0,command=chonlich)
    btnchonlich.place(x=842,y=184)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc)
    btnkhoiphuc.place(x=920,y=292)

    Entry(bg,font=("Baloo Tamma",11),width=36,textvariable=data_ten,bd=0,highlightthickness=0).place(x=575,y=80)
    Entry(bg,font=("Baloo Tamma",11),width=36,textvariable=data_email,bd=0,highlightthickness=0).place(x=575,y=134)
    Entry(bg,font=("Baloo Tamma",11),width=25,textvariable=data_ngaysinh,bd=0,highlightthickness=0).place(x=575,y=188)
    Entry(bg,font=("Baloo Tamma",11),width=28,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=652,y=294)

    
    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    f=Frame(bg)
    f.place(x=320,y=30)


    tv = ttk.Treeview(bg, columns=(1,2,3,4,5), show="headings")
    tv.column(1, width=30,anchor=CENTER)
    tv.column(2, width=80,anchor=CENTER)
    tv.column(3, width=150)
    tv.column(4, width=80)
    tv.column(5, width=240)

    tv.heading(1,text="STT")
    tv.heading(2,text="Mã GV")
    tv.heading(3,text="Tên giảng viên")
    tv.heading(4,text="Ngày sinh")
    tv.heading(5,text="Email")
    tv.place(x=370,y=340)
    tv.bind('<Double 1>', getrow)
    row=csdl_gv.banggv(makhoa)


    update(row)
    win.mainloop()

