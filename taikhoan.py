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
    def thongbaodd():
        win.destroy()
        diemdanhbu.main()
    def quaylai():
        win.destroy()
        main()
    def lichgiang():
        anhnen=bg.create_image(500,300,image=img_bg1)
        btnthongbao.destroy()
        lbgv.destroy()
        lbtk.destroy()
        lbe.destroy()
        btndangxuat1.destroy()
        btndoimatkhau.destroy()
        lbcg.destroy()
        lbstb.destroy()
        lbstb1.destroy()
        lbdd.destroy()
        btnthongbaodd.destroy()
        bglichgiang=Frame(bg,width=450,height=140,bg="#A672BB")
        bglichgiang.place(x=410,y=155)
        for i in range(len(l)):
            j=0
            Label(bglichgiang,text=l[i],width=20).grid(row=i,column=j,pady=10)
            Label(bglichgiang,text=m[i],width=35).grid(row=i,column=j+1,padx=10,pady=10)
            Label(bglichgiang,text=c[i],width=10).grid(row=i,column=j+2,pady=10)
        btnquaylai=Button(bg,image=ing_btnquaylai,bd=0,highlightthickness=0,command=quaylai)
        btnquaylai.place(x=836,y=537)
        
            

    def menuthongke():
        win.destroy()
        thongke.main()

    def menudiemdanh():
        win.destroy()
        diemdanhsv.main()

    def menuthemsv():
        win.destroy()
        them_sv_moi.main()

    def dangxuat():
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
    img_bg=ImageTk.PhotoImage(file="img/bgtaikhoan.png")
    img_bg1=ImageTk.PhotoImage(file="img/bgtaikhoan1.png")
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan1.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_btndangxuat1=ImageTk.PhotoImage(file="img/btndangxuat1.png")
    ing_btndoimatkhau=ImageTk.PhotoImage(file="img/btndoimatkhau.png")
    ing_btnthongbao=ImageTk.PhotoImage(file="img/btnthongbao.png")
    ing_btnquaylai=ImageTk.PhotoImage(file="img/btnquaylai.png")
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    makhoa=csdl.makhoa_tu_email(email)
    tenkhoa=csdl.tenkhoatuma(makhoa)

#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,command=menuthemsv)
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,command=menudiemdanh)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=44)

    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    lbgv=Label(bg,text=tengv,font=("Baloo Tamma",12),fg="black",bg="white")
    lbgv.place(x=560,y=155)
    
    lbtk=Label(bg,text=tenkhoa,font=("Baloo Tamma",12),fg="black",bg="white")
    lbtk.place(x=560,y=220)

    lbe=Label(bg,text=email,font=("Baloo Tamma",12),fg="black",bg="white")
    lbe.place(x=560,y=280)

    l=[]
    m=[]
    c=[]
    ngaydd=[]
    tenlopdd=[]
    tenmhdd=[]
    cadd=[]
    magv=csdl.tengv_thanh_ma(tengv)
    # csdl.cagiang(magv,l,m,c)
    # for i in range(len(l)):
    #     cagiang= "Bạn có lịch giảng lớp "+str(l[i])+" môn"+str(m[i])+" vào ca "+str(c[i])
    #     Label(bg,text=cagiang,font=("Baloo Tamma",12),fg="black",bg="white").place(x=560,y=343)
    # Label(bg,text="Bạn thực hiện việc điểm danh rất tốt",font=("Baloo Tamma",12),fg="black",bg="white").place(x=560,y=405)

    # btnthongbaodd=Button(bg,image=ing_btnthongbao,bd=0,highlightthickness=0)
    # btnthongbaodd.place(x=790,y=390)

    if csdl.cagiang(magv,l,m,c) == False:
        lbcg=Label(bg,text="Hôm nay, bạn không có tiết giảng",font=("Baloo Tamma",12),fg="black",bg="white")
        lbcg.place(x=560,y=343)
    else:
        lbcg=Label(bg,text="Hôm nay, bạn có lịch giảng !",font=("Baloo Tamma",12),fg="black",bg="white")
        lbcg.place(x=560,y=343)
        btnthongbao=Button(bg,image=ing_btnthongbao,bd=0,highlightthickness=0,command=lichgiang)
        btnthongbao.place(x=790,y=330)
        lbstb=Label(bg,text=len(l),fg="red",font=("Arial",10),bg="white")
        lbstb.place(x=822,y=330)

    if csdl.gvdiemdanh(magv,ngaydd,tenlopdd,tenmhdd,cadd)== False:
        lbdd=Label(bg,text="Bạn thực hiện việc điểm danh rất tốt",font=("Baloo Tamma",12),fg="black",bg="white")
        lbdd.place(x=560,y=405)
    else:
        lbdd=Label(bg,text="Có lẽ bạn đã quên điểm danh !",font=("Baloo Tamma",12),fg="black",bg="white")
        lbdd.place(x=560,y=405)
        
        btnthongbaodd=Button(bg,image=ing_btnthongbao,bd=0,highlightthickness=0,command=thongbaodd)
        btnthongbaodd.place(x=790,y=390)
        lbstb1=Label(bg,text=len(ngaydd),fg="red",font=("Arial",10),bg="white")
        lbstb1.place(x=822,y=390)

    btndoimatkhau=Button(bg,image=ing_btndoimatkhau,bd=0,highlightthickness=0)
    btndoimatkhau.place(x=672,y=539)

    btndangxuat1=Button(bg,image=ing_btndangxuat1,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat1.place(x=836,y=537)
    
    win.mainloop()

