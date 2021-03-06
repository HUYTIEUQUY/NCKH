from tkinter import *
from tkcalendar import *
from tkinter import ttk, messagebox
from tkinter import PhotoImage
from PIL import ImageTk
import csdl
import csdl_admin
import dangnhap
import socket
import admin_lop
import admin_thongke
import admin_chitiettkb
import admin_monhoc



def main():
    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)
    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())

        data_ma.set(item['values'][1])
        data_magv.set(item['values'][1])
        data_ten.set(item['values'][2])
        data_email.set(item['values'][3])
        data_sdt.set(item['values'][4])
        data_ghichu.set(item['values'][5])

    def khoiphuc():
        ndtimkiem.set("")
        data_email.set("")
        data_ma.set("")
        data_magv.set("")
        data_ten.set("")
        data_sdt.set("")
        data_ghichu.set("")
        row=csdl_admin.banggv(makhoa)
        update(row)

    def timkiem():
        row=csdl_admin.timkiem_gv(makhoa,ndtimkiem.get())
        update(row)

    def kt_dau_khoangcach(s):
        return bool(s and s.strip())
        
    def them():
        ma=data_ma.get()
        ten=data_ten.get()
        sdt=data_sdt.get()
        ghichu=data_ghichu.get()
        emailgv=ma+"@teacher.mku.edu.vn"
        if ma =="" or ten == "" or sdt=="":
            messagebox.showwarning("thông báo","Bạn hãy nhập đầy đủ dữ liệu")
        elif len(ma) < 6 or ma.isnumeric()== False:
            messagebox.showwarning("thông báo","Mã giảng viên phải ít nhất 6 kí tự và là số")
        elif len(sdt) <10 or sdt.isnumeric()== False:
            messagebox.showwarning("thông báo","Số điện thoại không đúng")
        elif kt_dau_khoangcach(data_ten.get())==False :
            messagebox.showwarning("thông báo","Dữ liệu tên giảng viên không hợp lệ")
        elif csdl_admin.KT_ma_tontai(ma) == True:
            csdl_admin.themgv(makhoa,ma,emailgv,ten,sdt,ghichu)
            messagebox.showinfo("thông báo","Đã thêm giảng viên vào danh sách")
            khoiphuc()
        
    def xoa():
        if data_ma.get()=="" or data_ten.get()=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu xoá. Bạn hãy click 2 lần vào dòng muốn xoá !")
        elif messagebox.askyesno("thông báo","Bạn thực sự muốn xoá"):
            if csdl_admin.kt_gv_tontai(data_ma.get()):
                csdl_admin.xoagv(data_ma.get(),data_email.get())
                khoiphuc()
            else:
                return


    def sua():
        if data_ma.get() != data_magv.get():
            messagebox.showwarning("thông báo","khổng thể sửa mã")
            data_ma.set(data_magv.get())
        elif data_magv.get()=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu sửa. Bạn hãy click 2 lần vào dòng muốn sửa !")
        elif data_ten.get()=="" or data_sdt.get()=="":
            messagebox.showwarning("thông báo","Bạn hãy nhập đầy đủ dữ liệu")
        elif kt_dau_khoangcach(data_ten.get())==False :
            messagebox.showwarning("thông báo","Dữ liệu tên giảng viên không hợp lệ")
        elif data_sdt.get().isnumeric()== False:
            messagebox.showwarning("thông báo","Số điện thoại không đúng")
        else:
            csdl_admin.suagv(data_magv.get(),data_ten.get(),data_sdt.get(),data_ghichu.get())
            messagebox.showinfo("thông báo","Đã sửa thành công")
            khoiphuc()
    def menuthongke():
        win.destroy()
        admin_thongke.main()
    def menumonhoc():
        win.destroy()
        admin_monhoc.main()
    def menutkb():
        win.destroy()
        admin_chitiettkb.main()
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
    data_ma=StringVar()
    data_ten=StringVar()
    data_email=StringVar()
    ndtimkiem=StringVar()
    data_magv=StringVar()
    data_sdt=StringVar()
    data_ghichu=StringVar()

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
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc)
    btnkhoiphuc.place(x=920,y=292)

    Entry(bg,font=("Baloo Tamma",11),width=36,textvariable=data_ma,bd=0,highlightthickness=0).place(x=575,y=75)
    Entry(bg,font=("Baloo Tamma",11),width=36,textvariable=data_ten,bd=0,highlightthickness=0).place(x=575,y=110)
    Entry(bg,font=("Baloo Tamma",11),width=36,textvariable=data_sdt,bd=0,highlightthickness=0).place(x=575,y=145)
    Entry(bg,font=("Baloo Tamma",11),width=36,textvariable=data_ghichu,bd=0,highlightthickness=0).place(x=575,y=178)
    Entry(bg,font=("Baloo Tamma",11),width=28,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=652,y=294)

   
    
    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)


    f=Frame(bg)
    f.place(x=320,y=30)


    tv = ttk.Treeview(bg, columns=(1,2,3,4,5,6), show="headings")
    tv.column(1, width=30,anchor=CENTER)
    tv.column(2, width=50,anchor=CENTER)
    tv.column(3, width=120)
    tv.column(4, width=200)
    tv.column(5, width=80,anchor=CENTER)
    tv.column(6, width=100)

    tv.heading(1,text="STT")
    tv.heading(2,text="Mã GV")
    tv.heading(3,text="Tên giảng viên")
    tv.heading(4,text="Email")
    tv.heading(5,text="Số điện thoại")
    tv.heading(6,text="Ghi chú")
    tv.place(x=370,y=340)
    tv.bind('<Double 1>', getrow)
    khoiphuc()
    win.mainloop()

if __name__ == '__main__':
    main()

