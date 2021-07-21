from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import socket
import csdl
import quanli_tkb
def tao_tkb():
    def tao():
        mlop=csdl.tenlop_thanh_ma(cb.get())
        if(csdl.KT_MaTKB(mlop)== []):
            csdl.tao_tkb(mlop)
            win.destroy()
            quanli_tkb.ql_tkb()
        else:
            if(messagebox.askyesno("thông báo","Thời khoá biểu đã tồn tại. Bạn có muốn cập nhật ?")):
                win.destroy()
                quanli_tkb.ql_tkb()
            else:
                return True


    win =Tk()
    win.title("Phần mềm điểm danh bằng nhận diện khuôn mặt")
    win.geometry("500x200")
    win.resizable(False,False)
    Label(win, text="Tạo thời khoá biểu ", font=("Times new roman",20,"bold"),fg="blue").pack()
    f=Frame(win,pady=50)
    f.pack()

    Label(f, text="Chọn lớp ",font=("Times new roman",15)).grid(row=0, column=0)

    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    makhoa=csdl.makhoa_tu_email(d[0])
    lop=csdl.lop_theo_khoa(makhoa)

    cb=Combobox(f,width=20,font=("Times new roman",15),values=lop)
    cb.current(0)
    cb.grid(row=0,column=1)

    Button(f,text="Tạo",fg="white",bg="blue",font=("Times new roman",12),command=tao).grid(row=0, column=3,padx=20,ipadx=20)
    win.mainloop()