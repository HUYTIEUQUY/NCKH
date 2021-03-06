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




def main():
    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)

    def capnhatbang(event):
        malop=csdl.tenlop_thanh_ma(data_lop.get())
        namhoc=csdl_admin.ma_namhoc(data_namhoc.get())
        row=csdl_admin.DS_tkb(malop,namhoc,data_hocky.get())
        update(row)

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
        malop=csdl.tenlop_thanh_ma(data_lop.get())
        namhoc=csdl_admin.ma_namhoc(data_namhoc.get())
        
        row=csdl_admin.timkiem_dongtkb(malop,ndtimkiem.get(),namhoc,data_hocky.get())
        update(row)

    def khoiphuc():
        ngaycu.set("")
        moncu.set("")
        gvcu.set("")
        cacu.set("")
        ndtimkiem.set("")
        data_ca.set("")
        data_gv.set("")
        data_mon.set("")
        data_ngay.set("")
        for i in range(5):
            ca[i].set(0)
        malop=csdl.tenlop_thanh_ma(data_lop.get())
        namhoc=csdl_admin.ma_namhoc(data_namhoc.get())
        row=csdl_admin.DS_tkb(malop,namhoc,data_hocky.get())
        update(row)
    def them():
        malop=csdl.tenlop_thanh_ma(data_lop.get())
        magv=csdl.tengv_thanh_ma(data_gv.get())
        mamh = csdl.tenmon_thanh_ma(data_mon.get())
        ngay=data_ngay.get()
        namhoc=csdl_admin.ma_namhoc(data_namhoc.get())
        hki=data_hocky.get()
        pp=data_loai.get()
        data_ca=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                data_ca += str(i)
        if len(data_ca)==2:
            ca1=data_ca[0:1]
            ca2=data_ca[1:2]
        else:
            ca1=ca2=data_ca

        if data_ca=="" or magv=="" or mamh=="" or ngay =="":
            messagebox.showerror("th??ng b??o","H??y ch???n ?????y ????? d??? li???u")
        elif(csdl_admin.KT_lichgiang(ngay,magv,ca1)!= None and csdl_admin.KT_lichgiang(ngay,magv,ca2)!= None):
            messagebox.showerror("th??ng b??o","Gi???ng vi??n ???? c?? l???ch d???y !")
        elif(csdl_admin.KT_lich_tkb(ngay,malop,data_ca)!= None):
            messagebox.showerror("th??ng b??o","L???p ???? c?? l???ch h???c !")
        else:
            csdl_admin.them_tkb(magv,malop,mamh,ngay,data_ca,namhoc,hki,pp)
            messagebox.showinfo("th??ng b??o", "???? th??m 1 d??ng v??o th???i kho?? bi???u ")
            khoiphuc()
            
    def sua():
        #d??? li???u ch??a c???p nh???t
        ngay_cu=ngaycu.get()
        mon_cu=csdl.tenmon_thanh_ma(moncu.get())
        gv_cu=csdl.tengv_thanh_ma(gvcu.get())
        ca_cu=cacu.get()
        # 
        #du li???u c???p nh???t
        malop=csdl.tenlop_thanh_ma(data_lop.get())
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
        
        if(ngaycu.get()== ""):
            messagebox.showerror("th??ng b??o","kh??ng t??m th???y d??? li???u c???n s???a ! B???n h??y nh???n 2 l???n v??o d??ng mu???n s???a , r???i s???a d??? li???u v?? nh???n n??t s???a")
        elif data_ca=="" or magv=="" or mamh=="" or ngay =="":
            messagebox.showerror("th??ng b??o","H??y ch???n ?????y ????? d??? li???u")
        elif(csdl_admin.KT_lichgiang(ngay,magv,ca1) != None and csdl_admin.KT_lichgiang(ngay,magv,ca2) != None):
            messagebox.showerror("th??ng b??o","Gi???ng vi??n ???? c?? l???ch d???y !")
        elif(csdl_admin.KT_lich_tkb(ngay,malop,data_ca)!= None):
            messagebox.showerror("th??ng b??o","L???p ???? c?? l???ch h???c !")
        else:
            csdl_admin.xoa_dong_tkb(ngay_cu,mon_cu,gv_cu,ca_cu)
            csdl_admin.them_tkb(data_matkb,magv,malop,mamh,ngay,data_ca)
            messagebox.showinfo("th??ng b??o", "???? th??m 1 d??ng v??o th???i kho?? bi???u ")
            khoiphuc()
               

    def xoa():
        magv=csdl.tengv_thanh_ma(data_gv.get())
        mamh = csdl.tenmon_thanh_ma(data_mon.get())
        ngay=data_ngay.get()
        data_ca=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                data_ca += str(i)
        if ngay=="":
            messagebox.showerror("th??ng b??o","Kh??ng t??m th???y d??? li???u c???n xo??.\n B???n h??y nh???n 2 l???n v??o d??ng mu???n xo?? v?? nh???n n??t 'xo??'")
        else:
            csdl_admin.xoa_dong_tkb(ngay,mamh,magv,data_ca)
            messagebox.showinfo("th??ng b??o","???? xo?? kh???i th???i kho?? bi???u")
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
        lb.config(text="|")
        btnchonlich.config(command=chonlich)
    def chonlich():
        cal = Calendar(lb,selectmode="day",year=2021,month=8,day=16,bg="white")
        cal.pack()
        btn=Button(f,image=img_btnchon,bg="white",command=lambda:chonngay(cal,btn),bd=0,highlightthickness=0)
        btn.pack()
        btnchonlich.config(command=tam)
   

    def tam():
        return

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
    
   
    data_lop=StringVar()
    

    data_gv=StringVar()
    data_mon=StringVar()
    data_ngay=StringVar()
    data_namhoc=StringVar()
    data_hocky=StringVar()
    data_ngay.set("")
    data_ca=StringVar()
    data_matkb=StringVar()

    lop=csdl.lop_theo_khoa(makhoa)
    gv=csdl.tim_gv_trong_khoa(makhoa)
    mon=csdl.mon_theo_khoa(makhoa)
    ndtimkiem=StringVar()
    ngaycu=StringVar()
    cacu=StringVar()
    moncu=StringVar()
    gvcu=StringVar()
    data_loai=StringVar()
    hocky=[1,2]
    loai=["l?? thuy???t","th???c h??nh"]
    namhoc=csdl_admin.namhoc()

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
    btntimkiem.place(x=881,y=313)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc)
    btnkhoiphuc.place(x=920,y=313)

    btnchonlich=Button(bg,image=img_btnchonlich,bd=0,highlightthickness=0,command=chonlich)
    btnchonlich.place(x=858,y=155)    
    
 
    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    cbnam =Combobox(bg,textvariable=data_namhoc,font=("Times new roman",12), width=20,values=namhoc)
    cbnam.current(0)
    cbnam.bind('<<ComboboxSelected>>', capnhatbang)
    cbnam.place(x=552,y=20)


    cbhk =Combobox(bg,textvariable=data_hocky,font=("Times new roman",12), width=6, values=hocky)
    cbhk.current(0)
    cbhk.bind('<<ComboboxSelected>>', capnhatbang)
    cbhk.place(x=829,y=20)

    cbloai =Combobox(bg,textvariable=data_loai,font=("Times new roman",12), width=7,values=loai)
    cbloai.current(0)
    cbloai.place(x=825,y=120)

    cblop =Combobox(bg,textvariable=data_lop,font=("Times new roman",12), width=40,values=lop)
    cblop.current(0)
    cblop.bind('<<ComboboxSelected>>', capnhatbang)
    cblop.place(x=552,y=55)

    Label(bg,font=("Baloo Tamma",11),bg="white",textvariable=data_ngay).place(x=616,y=155)

    cbgv =Combobox(bg,textvariable=data_gv,font=("Times new roman",11), width=35,values=gv)
    cbgv.place(x=552,y=90)
    Frame(bg,width=270,height=2,bg="white").place(x=552,y=90)
    Frame(bg,width=3,height=23,bg="white").place(x=552,y=90)
    Frame(bg,width=270,height=2,bg="white").place(x=552,y=112)

    cbmon =Combobox(bg,textvariable=data_mon,font=("Times new roman",11), width=25,values=mon)
    cbmon.place(x=552,y=124)
    Frame(bg,width=200,height=2,bg="white").place(x=552,y=124)
    Frame(bg,width=3,height=23,bg="white").place(x=552,y=124)
    Frame(bg,width=200,height=2,bg="white").place(x=552,y=146)

    
    ca=[]
    for i in range(5):
        option=IntVar()
        option.set(0)
        ca.append(option)

    Checkbutton(bg,text="Ca 1",font=("Times new roman",11),variable=ca[1],bg="white").place(x=605,y=187)
    Checkbutton(bg,text="Ca 2",font=("Times new roman",11),variable=ca[2],bg="white").place(x=680,y=187)
    Checkbutton(bg,text="Ca 3",font=("Times new roman",11),variable=ca[3],bg="white").place(x=755,y=187)
    Checkbutton(bg,text="Ca 4",font=("Times new roman",11),variable=ca[4],bg="white").place(x=820,y=187)


    f=Frame(bg)
    f.place(x=320,y=30)
    lb=Label(f)
    lb.pack()

    Entry(bg,font=("Baloo Tamma",11),width=28,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=652,y=318)

    tv = ttk.Treeview(bg, columns=(1,2,3,4,5), show="headings")
    tv.column(1, width=80,anchor=CENTER)
    tv.column(2, width=200,anchor=CENTER)
    tv.column(3, width=80)
    tv.column(4, width=150)
    tv.column(5, width=50,anchor=CENTER)
    

    tv.heading(1,text="Ng??y")
    tv.heading(2,text="M??n h???c")
    tv.heading(3,text="PP.Gi???ng")
    tv.heading(4,text="Gi???ng vi??n")
    tv.heading(5,text="Ca")
    
    tv.place(x=380,y=370)
    tv.bind('<Double 1>', getrow)

    

   
    khoiphuc()
    win.mainloop()


if __name__ == '__main__':
    main()
