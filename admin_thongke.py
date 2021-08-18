from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from types import coroutine
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
import admin_giangvien
import admin_chitiettkb
import admin_monhoc
import csdl_admin

def main():
    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)
    def reset():
        win.destroy()
        main()

    def timkiem():
        q=ndtimkiem.get()
        try:
            row=csdl.timkiem_diemdanh(gv.get(),ngay.get(),mh.get(),lop.get(),ca.get(),q)
            update(row)
        except:
            return
    def chon4(cb_ca):
        c=ca.get()
        Label(bg,text=c,font=("Baloo Tamma",12),bg="white").place(x=762,y=142)
        cb_ca.destroy()
        row =csdl.thongke(gv.get(),ngay.get(),mh.get(), lop.get() ,c)
        update(row)
        
    def chon3(cb_ngay):
        ng=ngay.get()
        data_ca=csdl.tim_ca_trong_diemdanh(gv.get(),lop.get(),mh.get(),ng)
        Label(bg,text=ng,font=("Baloo Tamma",12),bg="white").place(x=762,y=97)
        cb_ngay.destroy()
        cb_ca=Combobox(bg,textvariable=ca,font=("Baloo Tamma",12),values=data_ca,width=10)
        cb_ca.place(x=762,y=148)
        ngay.set(ng)
        btnchon.config(image=ing_btnxemthongke, command=lambda:chon4(cb_ca))
        

    def chon2(cb_mh):
        tenmon=mh.get()
        mamh=csdl.tenmon_thanh_ma(tenmon)
        data_ngay=csdl.tim_ngay_trong_diemdanh(gv.get(),lop.get(),mamh)
        Label(bg,text=tenmon,font=("Baloo Tamma",12),bg="white").place(x=468,y=192)
        cb_mh.destroy()
        cb_ngay=Combobox(bg,textvariable=ngay,font=("Baloo Tamma",12),values=data_ngay,width=10)
        cb_ngay.place(x=762,y=95)
        mh.set(mamh)
        btnchon.config(command=lambda:chon3(cb_ngay))

    def chon1(cb_lop):
        tenlop=lop.get()
        malop=csdl.tenlop_thanh_ma(tenlop)
        data_mh=csdl.tim_mon_trong_diemdanh(gv.get(),malop)
        Label(bg,text=tenlop,font=("Baloo Tamma",12),bg="white").place(x=468,y=142)
        cb_lop.destroy()
        cb_mh=Combobox(bg,textvariable=mh,font=("Baloo Tamma",12),values=data_mh,width=20)
        cb_mh.place(x=468,y=190)
        lop.set(malop)
        btnchon.config(command=lambda:chon2(cb_mh))

    def chon():
        tengv=gv.get()
        magv=csdl.tengv_thanh_ma(str(gv.get()))
        data_lop=csdl.tim_lop_trong_diemdanh(magv)
        Label(bg,text=tengv,font=("Baloo Tamma",12),bg="white").place(x=468,y=97)
        cb_gv.destroy()
        cb_lop=Combobox(bg,textvariable=lop,font=("Baloo Tamma",12),values=data_lop,width=20)
        cb_lop.place(x=468,y=142)
        gv.set(magv)
        btnchon.config(command=lambda:chon1(cb_lop))
        btnchonlai=Button(bg,image=ing_btnchonlai,bd=0,highlightthickness=0,command=reset)
        btnchonlai.place(x=869,y=207)
       
 
    def menulop():
        win.destroy()
        admin_lop.main()
    def menumonhoc():
        win.destroy()
        admin_monhoc.main()
    def menutkb():
        win.destroy()
        admin_chitiettkb.main()
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
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_thongke_admin.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_admin/btn_dangxuat.png")
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke1.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")
    ing_btnxemthongke=ImageTk.PhotoImage(file="img/btn_xemthongke.png")
    ing_btnchon=ImageTk.PhotoImage(file="img/btnchon.png")
    ing_btnchonlai=ImageTk.PhotoImage(file="img/chonlai.png")
    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    makhoa=csdl.makhoa_tu_email(email)
    tengv=csdl.tim_tengv_tu_email()
    data_gv=csdl.tim_gv_trong_khoa(makhoa)
   
    gv=StringVar()
    lop=StringVar()
    mh=StringVar()
    ngay=StringVar()
    ca=StringVar()
    ndtimkiem=StringVar()

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
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0,command=menutkb)
    menutkb.place(x=30,y=296)
    menumonhoc=Button(bg,image=img_menumonhoc,bd=0,highlightthickness=0,command=menumonhoc)
    menumonhoc.place(x=30,y=380)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,command=main)
    menuthongke.place(x=30,y=461)

 
    btnchon=Button(bg,image=ing_btnchon,bd=0,highlightthickness=0, activebackground="white",command=chon)
    btnchon.place(x=881,y=176)
    btntimkiem=Button(bg,image=img_btntimkiem,highlightthickness=0,bd=0,command=timkiem)
    btntimkiem.place(x=880,y=248)
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)
    
    cb_gv=Combobox(bg,textvariable=gv,font=("Baloo Tamma",12),values=data_gv,width=20)
    cb_gv.place(x=468,y=95)


    Entry(bg,font=("Baloo Tamma",12),width=28,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=615,y=248)
 
   
    
    
  

    tv = ttk.Treeview(bg, columns=(1,2,3), show="headings")
    tv.column(1, width=150 ,anchor=CENTER)
    tv.column(2, width=240)
    tv.column(3, width=150,anchor=CENTER)
    tv.heading(1,text="Mã số sinh viên")
    tv.heading(2,text="Họ và tên")
    tv.heading(3,text="Điểm danh")
    tv.place(x=370,y=300)
    
    win.mainloop()

if __name__ == '__main__':
    main()