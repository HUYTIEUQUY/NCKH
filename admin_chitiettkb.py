from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from mysql.connector import cursor
import csdl
import csdl_admin
from tkinter import messagebox
import dangnhap
import socket
import admin_lop
import admin_giangvien
import admin_thongke
import admin_monhoc
import admin_tkb



def main(matkb,malop):
    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)
    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        data_ngay.set(item['values'][1])
        data_mon.set(item['values'][2])
        data_gv.set(item['values'][3])
        data_ca.set(item['values'][4])

        ngaycu.set(item['values'][1])
        moncu.set(item['values'][2])
        gvcu.set(item['values'][3])
        cacu.set(item['values'][4])
        dataca=str(item['values'][4])
        
        
        for i in range(5):
            if dataca.find(str(i)) != -1:
                ca[i].set(1)
            else:
                ca[i].set(0)

    def timkiem():
        row=csdl_admin.timkiem_dongtkb(matkb,ndtimkiem.get())
        update(row)
    def khoiphuc():
        ndtimkiem.set("")
        data_ca.set("")
        data_gv.set("")
        data_mon.set("")
        data_ngay.set("")
        for i in range(5):
            ca[i].set(0)
        row=csdl_admin.DS_tkb(matkb)
        update(row)
    def them():
        magv=csdl.tengv_thanh_ma(data_gv.get())
        mamh = csdl.tenmon_thanh_ma(data_mon.get())
        ngay=data_ngay.get()
        data_ca=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                data_ca += str(i)
        if len(data_ca)==2:
            ca1=data_ca[0:1]
            ca2=data_ca[1:2]
        else:
            ca1=ca2=data_ca
        if(csdl_admin.KT_lichgiang(ngay,magv,ca1)== None and csdl_admin.KT_lichgiang(ngay,magv,ca2)== None):
            if(csdl_admin.KT_lich_tkb(ngay,malop,data_ca)== None):
                csdl_admin.them_tkb(matkb,magv,malop,mamh,ngay,data_ca)
                messagebox.showinfo("thông báo", "Đã thêm 1 dòng vào thời khoá biểu ")
                khoiphuc()
            else:
                messagebox.showerror("thông báo","Lớp đã có lịch học !")
        else:
            messagebox.showerror("thông báo","Giảng viên đã có lịch dạy !")
        khoiphuc()
    def sua():
        #dữ liệu chưa cập nhật
        ngay_cu=ngaycu.get()
        mon_cu=csdl.tenmon_thanh_ma(moncu.get())
        gv_cu=csdl.tengv_thanh_ma(gvcu.get())
        ca_cu=cacu.get()
        csdl_admin.xoa_dong_tkb(ngay_cu,mon_cu,gv_cu,ca_cu)
        #du liệu cập nhật
        magv=csdl.tengv_thanh_ma(data_gv.get())
        mamh = csdl.tenmon_thanh_ma(data_mon.get())
        ngay=data_ngay.get()
        data_ca=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                data_ca += str(i)


        if len(data_ca)==2:
            ca1=data_ca[0:1]
            ca2=data_ca[1:2]
        else:
            ca1=ca2=data_ca
        
        if(ngaycu.get()!= ""):
            if(csdl_admin.KT_lichgiang(ngay,magv,ca1)== None and csdl_admin.KT_lichgiang(ngay,magv,ca2)== None):
                if(csdl_admin.KT_lich_tkb(ngay,malop,data_ca)== None):
                    csdl_admin.them_tkb(matkb,magv,malop,mamh,ngay,data_ca)
                    
                    messagebox.showinfo("thông báo", "Đã thêm 1 dòng vào thời khoá biểu ")
                    khoiphuc()
                else:
                    messagebox.showerror("thông báo","Lớp đã có lịch học !")
                    csdl_admin.them_tkb(matkb,gv_cu,malop,mon_cu,ngay,ca_cu)
            else:
                messagebox.showerror("thông báo","Giảng viên đã có lịch dạy !")
                csdl_admin.them_tkb(matkb,gv_cu,malop,mon_cu,ngay,ca_cu)
        else:
            messagebox.showerror("thông báo","không tìm thấy dữ liệu cần sửa !")
            csdl_admin.them_tkb(matkb,gv_cu,malop,mon_cu,ngay,ca_cu)

    def xoa():
        magv=csdl.tengv_thanh_ma(data_gv.get())
        mamh = csdl.tenmon_thanh_ma(data_mon.get())
        ngay=data_ngay.get()
        data_ca=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                data_ca += str(i)
        csdl_admin.xoa_dong_tkb(ngay,mamh,magv,data_ca)
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
    def chonngay(cal,btn):
        data_ngay.set(csdl.dinh_dang_ngay(cal.get_date()))
        cal.destroy()
        btn.destroy()
        Label(f).pack()
    def chonlich():
        cal = Calendar(f,selectmode="day",year=2021,month=8,day=16,bg="white")
        cal.pack()
        btn=Button(f,image=img_btnchon,bg="white",command=lambda:chonngay(cal,btn),bd=0,highlightthickness=0)
        btn.pack()
    def trolai():
        win.destroy()
        admin_tkb.main()

    win=Tk()
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Menu tkinter")
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_chitiettkb.png")

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
    img_btnchonlich=ImageTk.PhotoImage(file="img_admin/chonlich.png")
    img_btntrolai=ImageTk.PhotoImage(file="img_admin/btn_trolai.png")
    img_btnchon=ImageTk.PhotoImage(file="img_admin/btn_chon.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    makhoa=csdl.makhoa_tu_email(email)
    tenlop=csdl_admin.ma_lop_thanh_ten(malop)
    data_gv=StringVar()
    data_mon=StringVar()
    data_ngay=StringVar()
    data_ngay.set("")
    data_ca=StringVar()
    gv=csdl.tim_gv_trong_khoa(makhoa)
    mon=csdl.mon_theo_khoa(makhoa)
    ndtimkiem=StringVar()
    ngaycu=StringVar()
    cacu=StringVar()
    moncu=StringVar()
    gvcu=StringVar()

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
    btnthem.place(x=487,y=247)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0,command=sua)
    btnsua.place(x=637,y=247)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=247)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,command=timkiem)
    btntimkiem.place(x=881,y=292)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc)
    btnkhoiphuc.place(x=920,y=292)
    btnchonlich=Button(bg,image=img_btnchonlich,bd=0,highlightthickness=0,command=chonlich)
    btnchonlich.place(x=858,y=165)
    btntrolai=Button(bg,image=img_btntrolai,bd=0,highlightthickness=0,command=trolai)
    btntrolai.place(x=950,y=2)
    
    
 
    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    Label(bg,text=tenlop,font=("Baloo Tamma",11),bg="white").place(x=616,y=40)
    Label(bg,text="",font=("Baloo Tamma",11),bg="white",textvariable=data_ngay).place(x=616,y=165)
    cbgv =Combobox(bg,textvariable=data_gv,font=("Times new roman",11), width=35,values=gv)
    cbgv.place(x=614,y=80)
    Frame(bg,width=270,height=2,bg="white").place(x=614,y=80)
    Frame(bg,width=3,height=25,bg="white").place(x=614,y=80)
    Frame(bg,width=270,height=2,bg="white").place(x=614,y=102)

    cbmon =Combobox(bg,textvariable=data_mon,font=("Times new roman",11), width=35,values=mon)
    cbmon.place(x=614,y=122)
    Frame(bg,width=270,height=2,bg="white").place(x=614,y=122)
    Frame(bg,width=3,height=25,bg="white").place(x=614,y=122)
    Frame(bg,width=270,height=2,bg="white").place(x=614,y=144)

    
    ca=[]
    for i in range(5):
        option=IntVar()
        option.set(0)
        ca.append(option)

    Checkbutton(bg,text="Ca 1",font=("Times new roman",11),variable=ca[1],bg="white").place(x=605,y=205)
    Checkbutton(bg,text="Ca 2",font=("Times new roman",11),variable=ca[2],bg="white").place(x=680,y=205)
    Checkbutton(bg,text="Ca 3",font=("Times new roman",11),variable=ca[3],bg="white").place(x=755,y=205)
    Checkbutton(bg,text="Ca 4",font=("Times new roman",11),variable=ca[4],bg="white").place(x=820,y=205)


    f=Frame(bg)
    f.place(x=320,y=30)
    
    Entry(bg,font=("Baloo Tamma",11),width=28,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=652,y=294)

    tv = ttk.Treeview(bg, columns=(1,2,3,4,5), show="headings")
    tv.column(1, width=30,anchor=CENTER)
    tv.column(2, width=80,anchor=CENTER)
    tv.column(3, width=240)
    tv.column(4, width=120)
    tv.column(5, width=50,anchor=CENTER)
    

    tv.heading(1,text="STT")
    tv.heading(2,text="Ngày")
    tv.heading(3,text="Môn học")
    tv.heading(4,text="Giảng viên")
    tv.heading(5,text="Ca")
    tv.place(x=400,y=340)
    tv.bind('<Double 1>', getrow)

    row=csdl_admin.DS_tkb(matkb)

   
    update(row)
    print(matkb)
    win.mainloop()

