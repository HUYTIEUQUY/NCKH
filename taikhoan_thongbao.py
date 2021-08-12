from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk
import csdl
import dangnhap
import socket
import them_sv_moi
import diemdanhsv
import thongke
import taikhoan


def main():
    
    def quaylai():
        win.destroy()
        taikhoan.main()  

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
    img_bg1=ImageTk.PhotoImage(file="img/bgtaikhoan1.png")
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan1.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
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
    anhnen=bg.create_image(500,300,image=img_bg1)

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

    bglichgiang=Frame(bg,width=450,height=140,bg="#A672BB")
    bglichgiang.place(x=410,y=155)


    l=[]
    m=[]
    c=[]
    tengv=csdl.tim_tengv_tu_email()
    magv=csdl.tengv_thanh_ma(tengv)
    csdl.cagiang(magv,l,m,c)
    for i in range(len(l)):
        j=0
        Label(bglichgiang,text=l[i],width=20).grid(row=i,column=j,pady=10)
        Label(bglichgiang,text=m[i],width=35).grid(row=i,column=j+1,padx=10,pady=10)
        Label(bglichgiang,text=c[i],width=10).grid(row=i,column=j+2,pady=10)
    btnquaylai=Button(bg,image=ing_btnquaylai,bd=0,highlightthickness=0,command=quaylai)
    btnquaylai.place(x=836,y=537)

    win.mainloop()

if __name__ == '__main__':
    main()