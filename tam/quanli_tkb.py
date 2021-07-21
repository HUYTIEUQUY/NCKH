from tkinter import * 
from tkcalendar import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import csdl_tkb
import csdl
import socket


def ql_tkb():
    d=[]
    with open("matkb.txt", "r") as f:
        d=f.read().split("\n")
    mtkb=d[0]
    mlop=d[1]
    ten_thiet_bi = socket.gethostname()
    k=[]
    with open(ten_thiet_bi+".txt","r") as file:
        k=file.read().split()
    makhoa=csdl.makhoa_tu_email(k[0])

    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)
    def timkiem():
        row=csdl_tkb.timkiem_tkb(txt_TK.get())
        update(row)

    def xoa():
        q.set("")
        row=csdl_tkb.DS_tkb(mtkb)
        update(row)

    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        data_ngay.set(item['values'][0])
        data_mh.set(item['values'][1])
        data_gv.set(item['values'][2])
        n.set(item['values'][0])
        m.set(item['values'][1])
        v.set(item['values'][2])
        c.set(item['values'][3])
        data_ca=str(item['values'][3])
        
        
        for i in range(5):
            if data_ca.find(str(i)) != -1:
                ca[i].set(1)
            else:
                ca[i].set(0)
        
    def themds():
        ngay=data_ngay.get()
        mon=csdl.tenmon_thanh_ma(data_mh.get())
        gv=csdl.tengv_thanh_ma(data_gv.get())
        #lấy ca
        a=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                a += str(i)
        
        if(csdl_tkb.KT_lichgiang(ngay,gv,a)== None):
            if(csdl_tkb.KT_lich_tkb(ngay,mlop,a)== None):
                csdl_tkb.them_tkb(mtkb,gv,mlop,mon,ngay,a)
                messagebox.showinfo("thông báo", "Đã thêm 1 dòng vào thời khoá biểu ")
                xoa()
            else:
                messagebox.showerror("thông báo","Lớp đã có lịch học !")
        else:
            messagebox.showerror("thông báo","Giảng viên đã có lịch dạy !")

        
        
    def suads():
        #dữ liệu chưa cập nhật
        ngaycu=n.get()
        mhcu=csdl.tenmon_thanh_ma(m.get())
        gvcu=csdl.tengv_thanh_ma(v.get())
        cacu=c.get()
        
        #dữ liệu cập nhật
        ngay=data_ngay.get()
        mon=csdl.tenmon_thanh_ma(data_mh.get())
        gv=csdl.tengv_thanh_ma(data_gv.get())
        #lấy ca
        a=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                a += str(i)

        if(csdl_tkb.KT_lichgiang(ngay,gv,a)== None):
            if(csdl_tkb.KT_lich_tkb(ngay,mlop,a)== None):
                csdl_tkb.xoa_dong_ds(ngaycu,mhcu,gvcu,cacu)
                csdl_tkb.them_tkb(mtkb,gv,mlop,mon,ngay,a)
                messagebox.showinfo("thông báo", "Đã cập nhật thành công ")
                xoa()
            else:
                messagebox.showerror("thông báo","Lớp đã có lịch học !")
        else:
            messagebox.showerror("thông báo","Giảng viên đã có lịch dạy !")

        
        

    def xoads():
        
        ngay=data_ngay.get()
        mon=csdl.tenmon_thanh_ma(data_mh.get())
        gv=csdl.tengv_thanh_ma(data_gv.get())
        a=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                a += str(i)
        if messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá dòng dữ liệu này ?") :
            csdl_tkb.xoa_dong_ds(ngay,mon,gv,a)
            xoa()
        else:
            return True


    def chonngay():
        data_ngay.set(csdl.dinh_dang_ngay(cal.get_date()))
        


    win = Tk()

    l=Label(win, text="Thời Khoá biểu" ,font=("Times new roman",20,"bold"),fg="blue")
    lf1= LabelFrame(win,text="Danh sách thời khoá biểu",height=120)
    lf3= LabelFrame(win,text="Thao tác dữ liệu",height=120)
    
    f1=Frame(lf1)
    f1.pack(pady=10)
    f2=Frame(lf1)
    f2.pack()
    

    l.pack(pady=20)
    lf1.pack(fill="both" ,expand="yes", padx=20, pady=10)
    lf3.pack(fill="both" ,expand="yes", padx=20, pady=10)

    row=csdl_tkb.DS_tkb(mtkb)
    tv = ttk.Treeview(f2, columns=(1,2,3,4), show="headings")
    tv.pack()
    tv.heading(1,text="Ngày" )
    tv.heading(2,text="Môn học")
    tv.heading(3,text="Giảng viên")
    tv.heading(4,text="Ca")

    tv.bind('<Double 1>', getrow)

    update(row)
    tenlop=csdl_tkb.ma_lop_thanh_ten(mlop)
    Label(f1,text="Lớp :",font=("Times new roman",14,"bold")).pack(side="left")
    Label(f1,text=tenlop,font=("Times new roman",14)).pack(side="left")
    Frame(f1).pack(side="left",padx=80, pady=3)
    #tìm kiếm
    lbl= Label(f1, text="Tìm kiếm" )
    lbl.pack(side=tk.LEFT, padx=20)
    q=StringVar()
    txt_TK= Entry(f1, textvariable = q,font=("Times new roman",14))
    txt_TK.pack(side=tk.LEFT)
    Button(f1,text="Tìm kiếm",command=timkiem,bg="blue", fg="white").pack(side=tk.LEFT)
    Button(f1,text="Khôi phục",bg="blue", fg="white" ,command=xoa).pack(side=tk.RIGHT, padx=6)

    # Sửa , xoá dl
    f4=Frame(lf3)
    f4.pack(side=tk.LEFT,padx=10)
    cal = Calendar(f4,selectmode="day",year=2021,month=7,day=16)
    cal.grid(row=0,column=0)
    Button(f4,text="chọn ngày",bg="blue", fg="white", command=chonngay).grid(row=1,column=0, pady=3)


    f5=Frame(lf3)
    f5.pack(side=tk.LEFT)

    lb_l=Label(f5,text="Ngày :",font=("Times new roman",14,"bold"))
    lb_l.grid(row=0,column=0, padx=5, pady=3)
    data_ngay=StringVar()
    txt_ngay= Label(f5,textvariable=data_ngay, width=30,font=("Times new roman",14))
    txt_ngay.grid(row=0,column=1,padx=5, pady=3)
    

    lb_mh=Label(f5,text="Môn học :",font=("Times new roman",14,"bold"))
    lb_mh.grid(row=1,column=0, padx=5, pady=3)
    d=csdl.mon_theo_khoa(makhoa)
    data_mh=StringVar()
    txt_mh= ttk.Combobox(f5,textvariable=data_mh,font=("Times new roman",14), width=30 ,values=d)
    txt_mh.current(0)
    txt_mh.grid(row=1,column=1,padx=5, pady=3)

    lb_gv=Label(f5,text="Giảng viên :",font=("Times new roman",14,"bold"))
    lb_gv.grid(row=2,column=0, padx=5, pady=3)
    g=csdl.tim_gv_trong_khoa(makhoa)
    data_gv=StringVar()
    txt_gv=ttk.Combobox(f5,textvariable=data_gv,font=("Times new roman",14), width=30,values=g)
    txt_gv.current(0)
    txt_gv.grid(row=2,column=1,padx=5, pady=3)

    lb_ca=Label(f5,text="Ca :",font=("Times new roman",14,"bold"))
    lb_ca.grid(row=3,column=0, padx=5, pady=3)
    m=StringVar()
    n=StringVar()
    v=StringVar()
    c=StringVar()
    ca=[]
    for i in range(5):
        option=IntVar()
        option.set(0)
        ca.append(option)

    Checkbutton(f5,text="Ca 1",font=("Times new roman",14),variable=ca[1]).grid(row=3, column=1,padx=20)
    Checkbutton(f5,text="Ca 2",font=("Times new roman",14),variable=ca[2]).grid(row=3, column=2,padx=20)
    Checkbutton(f5,text="Ca 3",font=("Times new roman",14),variable=ca[3]).grid(row=3, column=3,padx=20)
    Checkbutton(f5,text="Ca 4",font=("Times new roman",14),variable=ca[4]).grid(row=3, column=4,padx=20)

    f6= Frame(lf3)
    f6.pack(side="bottom")
    Button(f6,text="Thêm", fg="black" , bg= "green",width=15,command=themds).grid(row=0,column=2, padx=5, pady=20)
    Button(f6,text="Sửa", fg="black" , bg= "yellow",width=15,command=suads).grid(row=0,column=3, padx=5, pady=20)
    Button(f6,text="xoá", fg="black" , bg= "red",width=15,command=xoads).grid(row=0,column=4, padx=5, pady=20)

    win.title("Phần mềm điểm danh bằng nhận dạng gương mặt")
    win.geometry("1600x820")
    win.mainloop()