from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from mysql.connector import cursor
import csdl
import csdl_tkb
from tkinter import messagebox
import dangnhap
import socket
import mysql.connector
import pickle
import cv2
import face_recognition
import admin_lop
import admin_giangvien
import admin_thongke
import admin_monhoc



def main(matkb):
    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)
    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        data_lop.set(item['values'][2])
        data_matkb.set(item['values'][1])
    def timkiem():
        row=csdl_tkb.timkiem_tkb(makhoa,ndtimkiem.get())
        update(row)
    def khoiphuc():
        ndtimkiem.set("")
        row=csdl_tkb.bangtkb(makhoa)
        update(row)
    def them():
        malop=csdl.tenlop_thanh_ma(data_lop.get())
        ngaylap=csdl.ngay()
        csdl_tkb.themtkb(malop,ngaylap)
        khoiphuc()
    def sua():
        malop=csdl.tenlop_thanh_ma(data_lop.get())
        csdl_tkb.suatkb(data_matkb.get(),malop)
        khoiphuc()
    def xoa():
        if(csdl_tkb.kt_chitiettkb(data_matkb.get())!=[]):
            messagebox.showerror("thông báo","Chi tiết thời khoá biểu vẫn đang tồn tại, Không xoá được")
        else:
            csdl_tkb.xoatkb(data_matkb.get())
            messagebox.showinfo("thông báo","xoá thành công")
            khoiphuc()
    def menuthongke():
        win.destroy()
        admin_thongke.main()
    def menumonhoc():
        win.destroy()
        admin_monhoc.main()
    def menulop():
        win.destroy()
        admin_lop.main()
    def menugiangvien():
        win.destroy()
        admin_giangvien.main()
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
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb1.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke.png")
    img_btnthem=ImageTk.PhotoImage(file="img_admin/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_admin/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_admin/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")
    img_btnxemct=ImageTk.PhotoImage(file="img_admin/btn_xem.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    makhoa=csdl.makhoa_tu_email(email)
    tenkhoa=csdl.tenkhoatuma(makhoa)
    lop=csdl.lop_theo_khoa(makhoa)
    data_lop=StringVar()
    ndtimkiem=StringVar()
    data_matkb=StringVar()
#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menudangxuat=Button(bg,image=img_menudangxuat,bd=0,highlightthickness=0,command=menudangxuat)
    menudangxuat.place(x=248,y=44)
    menulophoc=Button(bg,image=img_menulophoc,bd=0,highlightthickness=0,command=menulop)
    menulophoc.place(x=30,y=128)
    menugiangvien=Button(bg,image=img_menugiangvien,bd=0,highlightthickness=0,command=menugiangvien)
    menugiangvien.place(x=30,y=212)
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0,command=main)
    menutkb.place(x=30,y=296)
    menumonhoc=Button(bg,image=img_menumonhoc,bd=0,highlightthickness=0,command=menumonhoc)
    menumonhoc.place(x=30,y=380)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=30,y=461)

    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command=them)
    btnthem.place(x=550,y=237)
    btnxem=Button(bg,image=img_btnxemct,bd=0,highlightthickness=0)
    btnxem.place(x=430,y=237)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0,command=sua)
    btnsua.place(x=670,y=237)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=790,y=237)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,command=timkiem)
    btntimkiem.place(x=881,y=292)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc)
    btnkhoiphuc.place(x=920,y=292)


 
    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    Label(bg,text=tenkhoa,font=("Baloo Tamma",11),bg="white").place(x=570,y=77)
    
    cb_lop=Combobox(bg,textvariable=data_lop,font=("Baloo Tamma",12),values=lop,width=30)
    cb_lop.current(0)
    cb_lop.place(x=570,y=130)
    Entry(bg,font=("Baloo Tamma",11),width=28,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=652,y=294)



    tv = ttk.Treeview(bg, columns=(1,2,3,4), show="headings")
    tv.column(1, width=30,anchor=CENTER)
    tv.column(2, width=80,anchor=CENTER)
    tv.column(3, width=240)
    tv.column(4, width=120)
    

    tv.heading(1,text="STT")
    tv.heading(2,text="Mã TKB")
    tv.heading(3,text="Lớp")
    tv.heading(4,text="Ngày lập")
    tv.place(x=420,y=340)
    tv.bind('<Double 1>', getrow)

    row=csdl_tkb.bangtkb(makhoa)
    update(row)
    win.mainloop()

