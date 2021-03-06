from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import ImageTk
import csdl
import csdl_admin
from tkinter import messagebox
import dangnhap
import socket
import string
import admin_lop
import admin_giangvien
import admin_thongke
import admin_chitiettkb
import string


def main():
    def khoiphuc():
        ndtimkiem.set("")
        data_mamon.set("")
        data_tenmon.set("")
        data_sotietlt.set("")
        data_sotietth.set("")
        row=csdl_admin.bangmon(makhoa)
        update(row)

    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)

    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        data_tenmon.set(item['values'][2])
        data_mamon.set(item['values'][1])
        data_mamonsx.set(item['values'][1])
        data_sotietlt.set(item['values'][3])
        data_sotietth.set(item['values'][4])

    def kt_dau_khoangcach(s):
        return bool(s and s.strip())

    def kt_nhap(ma,ten,lt,th):
        if ma=="" or ten=="" or lt=="" or th=="" :
            messagebox.showwarning("thông báo","Hãy nhập đầy đủ dữ liệu")
        elif len(str(ma)) <6 or ma.isnumeric()== False :
            messagebox.showerror("thông báo","Mã môn học phải ít nhất 6 kí tự và là số")
            return False
        
        elif kt_dau_khoangcach(ten)==False:
            messagebox.showwarning("thông báo","Dữ liệu tên môn học không hợp lệ")
            return False
        elif lt.isnumeric()== False or th.isnumeric()== False:
            messagebox.showwarning("thông báo","Dữ liệu không hợp lệ")
        elif csdl_admin.kt_ma_mh(ma) !=[]:
            messagebox.showerror("thông báo","Mã môn học đã tồn tại")
            return False
        elif csdl_admin.kt_ten_mh(ten) != None:
            messagebox.showerror("thông báo","Môn học này đã tồn tại")
            return False
        else:
            return True

    def them():
        ten=data_tenmon.get()
        ma=data_mamon.get()
        lt=data_sotietlt.get()
        th=data_sotietth.get()
        if kt_nhap(ma,ten,lt,th) == True:
            csdl_admin.themmon(ma,makhoa,ten,lt,th)
            messagebox.showinfo("thông báo","Thêm '"+ten+"' thành công")
            khoiphuc()
    def xoa():
        ma=data_mamon.get()

        if data_mamonsx.get()== "":
            messagebox.showwarning("thông báo","Chưa có dữ liệu để xoá\nHãy nhấn 2 lần vào dòng dữ liệu muốn xoá và nhấn nút 'xoá'")
        elif messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá"):
            csdl_admin.xoamon(ma)
            khoiphuc()
        else: 
            return True

    def sua():
        ma=data_mamon.get()
        ten=data_tenmon.get()
        lt=data_sotietlt.get()
        th=data_sotietth.get()
        ten=str(ten).replace("  "," ")
        if data_mamonsx.get() == "" :
            messagebox.showerror("thông báo","Bạn chưa có dữ liệu sửa. Hãy nhấn 2 lần vào dòng muốn sửa, thay đổi tên và nhấn nút 'sửa'")
        elif ma!=data_mamonsx.get():
            messagebox.showwarning("thông báo","Bạn không thể sửa mã môn học")
            data_mamon.set(data_mamonsx.get())
        elif ten=="" or lt=="" or th=="" :
            messagebox.showwarning("thông báo","Hãy nhập đầy đủ dữ liệu")
        elif kt_dau_khoangcach(ten)==False :
            messagebox.showwarning("thông báo","Dữ liệu tên môn học không hợp lệ")
        elif lt.isnumeric()== False or th.isnumeric()== False:
            messagebox.showwarning("thông báo","Dữ liệu không hợp lệ")
        elif csdl_admin.kt_ten_mh(ten) != None and csdl_admin.kt_ten_mh(ten) != ma :
            messagebox.showerror("thông báo","Môn học này đã tồn tại")
        else:
            csdl_admin.suamon(ma,ten,lt,th)
            khoiphuc()
            messagebox.showinfo("thông báo","Sửa thành công")


    def timkiem():
        row=csdl_admin.timmon(makhoa,ndtimkiem.get())
        update(row)
    def menuthongke():
        win.destroy()
        admin_thongke.main()
    def menumonhoc():
        win.destroy()
        main()
    def menutkb():
        win.destroy()
        admin_chitiettkb.main()
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
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_monhoc.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_admin/btn_dangxuat.png")
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke.png")
    img_btnthem=ImageTk.PhotoImage(file="img_admin/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_admin/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_admin/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc1.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")
    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    makhoa=csdl.makhoa_tu_email(email)
    data_tenmon=StringVar()
    data_mamon=StringVar()
    data_sotietlt=StringVar()
    data_sotietth=StringVar()
    data_mamonsx=StringVar()
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
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=30,y=461)

    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command=them)
    btnthem.place(x=487,y=230)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0,command=sua)
    btnsua.place(x=637,y=230)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=230)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,command=timkiem)
    btntimkiem.place(x=881,y=315)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc)
    btnkhoiphuc.place(x=920,y=315)

 
    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    tenkhoa=csdl.tenkhoatuma(makhoa)
    
    Entry(bg,font=("Baloo Tamma",11),width=35,fg="black",bg="white",textvariable=data_mamon,bd=0,highlightthickness=0).place(x=590,y=72)

    Entry(bg,font=("Baloo Tamma",11),width=35,textvariable=data_tenmon,bd=0,highlightthickness=0).place(x=590,y=107)
    Entry(bg,font=("Baloo Tamma",11),width=35,textvariable=data_sotietlt,bd=0,highlightthickness=0).place(x=590,y=142)
    Entry(bg,font=("Baloo Tamma",11),width=35,textvariable=data_sotietth,bd=0,highlightthickness=0).place(x=590,y=177)
    Entry(bg,font=("Baloo Tamma",11),width=28,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=652,y=315)

    tv = ttk.Treeview(bg, columns=(1,2,3,4,5), show="headings")
    tv.column(1, width=50,anchor=CENTER)
    tv.column(2, width=80,anchor=CENTER)
    tv.column(3, width=240)
    tv.column(4, width=100,anchor=CENTER)
    tv.column(5, width=100,anchor=CENTER)

    tv.heading(1,text="STT")
    tv.heading(2,text="Mã môn")
    tv.heading(3,text="Tên môn")
    tv.heading(4,text="Số tiết lý thuyết")
    tv.heading(5,text="Số tiết thực hành")
    tv.place(x=368,y=350)

    tv.bind('<Double 1>', getrow)

    khoiphuc()
    win.mainloop()


if __name__ == '__main__':
    main()
