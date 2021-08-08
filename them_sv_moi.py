from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os
import shutil
from mysql.connector.errors import ProgrammingError
import csdl
from tkinter import messagebox
import dangnhap
import socket
import mysql.connector
import pickle
import cv2
import face_recognition
import diemdanhsv
import thongke
import taikhoan
import re
import xlsxwriter




def main():
    
    def khoiphuc():
        ma.set("")
        ten.set("")
        malop=csdl.tenlop_thanh_ma(cb_lop.get())
        row=csdl.danhsachsinhvien(malop)
        update(row)
    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)

    def capnhat(event):
        malop=csdl.tenlop_thanh_ma(cb_lop.get())
        row=csdl.danhsachsinhvien(malop)
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)

    def timkiem():
        malop=csdl.tenlop_thanh_ma(lop.get())
        row=csdl.timsv(malop,ndtimkiem.get())
        update(row)

    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        ten.set(item['values'][2])
        ma.set(item['values'][1])
        macu.set(item['values'][1])
        manganh=csdl.anh(ma.get())
        anh=manganh[0]
        gananh(anh)

    def gananh(s):
        manganh=s.split()
        for i in range(5):
            img=Image.open("img_anhsv/"+manganh[i])
            img.thumbnail((100,100))
            img=ImageTk.PhotoImage(img)
            
            if(i==0):
                lb1.config(image=img)
                lb1.image=img
            if(i==1):
                lb2.config(image=img)
                lb2.image=img
            if(i==2):
                lb3.config(image=img)
                lb3.image=img
            if(i==3):
                lb4.config(image=img)
                lb4.image=img
            if(i==4):
                lb5.config(image=img)
                lb5.image=img
            



    a=[]
    
    def khong_dau(s):
        s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
        s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
        s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
        s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
        s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
        s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
        s = re.sub(r'[ìíịỉĩ]', 'i', s)
        s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
        s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
        s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
        s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
        s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
        s = re.sub(r'[Đ]', 'D', s)
        s = re.sub(r'[đ]', 'd', s)
        return s

    def sua_anh(lb,i,btn):
        a.pop(i-1)
        print(a)
        chonanh(lb,i,btn)

    def sua():
        if(ma.get()!=macu.get()):
            messagebox.showerror("thông báo","Bạn không được sửa mã")
        else:
            masv=ma.get()
            tensv=ten.get()
            malop=csdl.tenlop_thanh_ma(cb_lop.get())
            csdl.suasv(masv,tensv,malop)
            xoa_sv_matran(masv)
            suamatran()
            messagebox.showinfo("thông báo","Bạn đã sửa thành công")

    def suamatran():
        id=ma.get()
        namemahoa=khong_dau(ten.get())
        lop=cb_lop.get().replace(" ","_")
        lopmahoa=khong_dau(lop)
        try:
            f=open("mahoa/"+lopmahoa+".pkl","rb")
            ref_dictt=pickle.load(f)
            f.close()
        except:
            ref_dictt={}
        ref_dictt[id]=namemahoa
        f=open("mahoa/"+lopmahoa+".pkl","wb")
        pickle.dump(ref_dictt,f)
        f.close()
        try:
            f=open("mahoa/"+lopmahoa+"mahoa.pkl","rb")
            embed_dictt=pickle.load(f)
            f.close()
        except:
            embed_dictt={}
        
        
        anh=""
        for i in range(len(a)):
            anh=anh+" "+str(a[i])
            file1_image = face_recognition.load_image_file("img_anhsv/"+a[i])
            file1_face_encoding = face_recognition.face_encodings(file1_image)[0]
            if id in embed_dictt:
                embed_dictt[id]+=[file1_face_encoding]
            else:
                embed_dictt[id]=[file1_face_encoding]
        

        f=open("mahoa/"+lopmahoa+"mahoa.pkl","wb")
        pickle.dump(embed_dictt,f)
        f.close()


    def xoa():
        masv=ma.get()
        if messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá"):
            csdl.xoasv(masv)# xoá sv trên database
            khoiphuc()
            xoa_sv_matran(masv)#xoá mahoa anh 
            xoaanh(masv)# xoá anh
            resetanh()
        else: 
            return True
        
    def xoa_sv_matran(masv):
        tenlop=lop.get().replace(" ","_")
        lopmahoa=khong_dau(tenlop)
        with open("mahoa/"+str(lopmahoa)+"mahoa.pkl","rb") as f:
            ref_dictt=pickle.load(f)
            ref_dictt.pop(masv)
        file= open("mahoa/"+str(lopmahoa)+"mahoa.pkl","wb") 
        pickle.dump(ref_dictt,file)
        file.close()
       
        with open("mahoa/"+str(lopmahoa)+".pkl","rb") as f:
            ref_dictt=pickle.load(f)
            ref_dictt.pop(masv)
        file= open("mahoa/"+str(lopmahoa)+".pkl","wb") 
        pickle.dump(ref_dictt,file)
        file.close()

    def xoaanh(masv):
        for i in range(5):
            os.remove("img_anhsv/"+str(masv)+str(i+1)+".png")

    def chonanh(lb,i,btn):
        x= filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All file","*.*")))
        shutil.copyfile(x,"./img_anhsv/"+str(ma.get())+str(i)+".png")

        a.insert(i-1,str(ma.get())+str(i)+".png")
        img=Image.open(x)
        img.thumbnail((80,100))
        img=ImageTk.PhotoImage(img)
        lb.config(image=img)
        lb.image=img
        btn.config(command=lambda:sua_anh(lb,i,btn) )
         
        
        
    def menutaikhoan():
        win.destroy()
        taikhoan.main()
    def menuthongke():
        win.destroy()
        thongke.main()
    def menudiemdanh():
        win.destroy()
        diemdanhsv.main()
    def dangxuat():
        ten_thiet_bi = socket.gethostname()
        file=open(ten_thiet_bi+".txt","w")
        file.write("")
        file.close()
        win.destroy()
        dangnhap.main()

    def resetanh():
        lb1.config(image="")
        img=Image.open("aa.jpg")
        img.thumbnail((100,100))
        img=ImageTk.PhotoImage(img)
        
        lb1.config(image=img)
        lb1.image=img

        lb2.config(image=img)
        lb2.image=img

        lb3.config(image=img)
        lb3.image=img

        lb4.config(image=img)
        lb4.image=img

        lb5.config(image=img)
        lb5.image=img
    
    def themdlkhuonmat():
        id=txt_masv.get()
        name=txt_hoten.get()
        namemahoa=khong_dau(name)
        malop=csdl.tenlop_thanh_ma(cb_lop.get())
        #thêm id , name vào co sở dữ liệu
        # insertOrUpdate(id,name,malop)

        lop=cb_lop.get().replace(" ","_")
        lopmahoa=khong_dau(lop)
        try:
            f=open("mahoa/"+lopmahoa+".pkl","rb")
            ref_dictt=pickle.load(f)
            f.close()
        except:
            ref_dictt={}
        ref_dictt[id]=namemahoa
        f=open("mahoa/"+lopmahoa+".pkl","wb")
        pickle.dump(ref_dictt,f)
        f.close()
        try:
            f=open("mahoa/"+lopmahoa+"mahoa.pkl","rb")
            embed_dictt=pickle.load(f)
            f.close()
        except:
            embed_dictt={}
        
        
        anh=""
        for i in range(len(a)):
            anh=anh+" "+str(a[i])
            file1_image = face_recognition.load_image_file("img_anhsv/"+a[i])
            file1_face_encoding = face_recognition.face_encodings(file1_image)[0]
            if id in embed_dictt:
                embed_dictt[id]+=[file1_face_encoding]
            else:
                embed_dictt[id]=[file1_face_encoding]
        

        f=open("mahoa/"+lopmahoa+"mahoa.pkl","wb")
        pickle.dump(embed_dictt,f)
        f.close()
        csdl.insertOrUpdate(id,name,malop,anh)

        ma.set("")
        ten.set("")
        resetanh()
        malop=csdl.tenlop_thanh_ma(cb_lop.get())
        row=csdl.danhsachsinhvien(malop)
        cb_lop.bind('<<ComboboxSelected>>', capnhat)
        khoiphuc()
        messagebox.showinfo("thông báo","Đã thêm sinh viên vào danh sách")
        # for i in range(5):
        #     key = cv2. waitKey(1)
        #     webcam = cv2.VideoCapture(0)
        #     while True:
            
        #         check, frame = webcam.read()
        #         cv2.imshow("Capturing", frame)
        #         # Thay đổi kích thước trong opencv
        #         #frame: màn hình là hình ảnh đầu vào
        #         #(0, 0), fx=0.25, fy=0.25 : kích thước mong muốn cho hình ảnh đầu
        #         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        #         rgb_small_frame = small_frame[:, :, ::-1] # Chuyển đổi hình ảnh từ màu BGR (OpenCV sử dụng) sang màu RGB (face_recognition sử dụng)
        
        #         key = cv2.waitKey(1)
        #         if key == ord('s') : 
        #             face_locations = face_recognition.face_locations(rgb_small_frame)
        #             if face_locations != []: #nếu có khuôn mặt
        #                 face_encoding = face_recognition.face_encodings(frame)[0] #mã hoá và lưu vào biến face_encoding
        #                 if id in embed_dictt: #Nếu id đã tồn tại thì cộng thêm hình ảnh đã mã hoá vào
        #                     embed_dictt[id]+=[face_encoding]
        #                 else:#Nếu chưa tồn tại thì khởi tạo với "id"="dữ liệu hình ảnh mã hoá"
        #                     embed_dictt[id]=[face_encoding]
        #                 if(i==4):
        #                     messagebox.showinfo("thông báo", "Đã lưu mã hoá khuôn mặt")
        #                 webcam.release()
                        
        #                 cv2.destroyAllWindows()
        #                 break
                    
        #         elif key == ord('q'):
        #             print("Turning off camera.")
        #             webcam.release()
        #             print("Camera off.")
        #             print("Program ended.")
        #             cv2.destroyAllWindows() # thoát khỏi camera
        #             break
                    


        # f=open("mahoa/"+lop+"mahoa.pkl","wb")
        # pickle.dump(embed_dictt,f)
        # f.close()

    win=Tk()
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Menu tkinter")
    img_bg=ImageTk.PhotoImage(file="img/bg_themdl.png")
 
    ing_btnchonanh=ImageTk.PhotoImage(file="img/chon_anh.png")
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_chonanh=ImageTk.PhotoImage(file="img/btnchhonanh.png")
    img_btnthem=ImageTk.PhotoImage(file="img_admin/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_admin/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_admin/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")

    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    #chọn lớp
    ten_thiet_bi = socket.gethostname()
    d=[]
    ma=StringVar()
    macu=StringVar()
    ten=StringVar()
    lop=StringVar()
    ndtimkiem=StringVar()
    

    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    makhoa=csdl.makhoa_tu_email(d[0])
    data_lop=csdl.lop_theo_khoa(makhoa)

    


    cb_lop=Combobox(bg,width=27,values=data_lop, font=("Baloo Tamma",12),textvariable=lop)
    cb_lop.current(1)
    cb_lop.place(x=580,y=12)

    cb_lop.bind('<<ComboboxSelected>>', capnhat)
    Frame(bg,width=287,height=5,bg= "white").place(x=570,y=12)
    Frame(bg,width=276,height=5,bg= "white").place(x=570,y=32)
    Frame(bg,width=5,height=20,bg= "white").place(x=577,y=12)

    
    txt_masv=Entry(bg,width=30,bd=0,font=("Baloo Tamma",12),textvariable=ma,highlightthickness=0)
    txt_masv.place(x=578,y=48)
    txt_timkiem=Entry(bg,width=25,bd=0,font=("Baloo Tamma",12),textvariable=ndtimkiem,highlightthickness=0)
    txt_timkiem.place(x=650,y=308)

    txt_hoten=Entry(bg,width=30,bd=0,font=("Baloo Tamma",12),textvariable=ten,highlightthickness=0)
    txt_hoten.place(x=578,y=81)


    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command=themdlkhuonmat)
    btnthem.place(x=487,y=260)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0,command=sua)
    btnsua.place(x=637,y=260)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=260)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,command=timkiem)
    btntimkiem.place(x=881,y=305)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc)
    btnkhoiphuc.place(x=915,y=305)


   

    

    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0)
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,command=menudiemdanh)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,command=menutaikhoan)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=44)

    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)
    

        
    f1=Frame(bg,bg="white",width=100,height=120)
    f1.place(x=322,y=120)
    f2=Frame(bg,bg="white",width=100,height=120)
    f2.place(x=458,y=120)
    f3=Frame(bg,bg="white",width=100,height=120)
    f3.place(x=594,y=120)
    f4=Frame(bg,bg="white",width=100,height=120)
    f4.place(x=730,y=120)
    f5=Frame(bg,bg="white",width=100,height=120)
    f5.place(x=866,y=120)

    lb1=Label(f1,bg="white")
    lb1.pack()
    lb2=Label(f2,bg="white")
    lb2.pack()
    lb3=Label(f3,bg="white")
    lb3.pack()
    lb4=Label(f4,bg="white")
    lb4.pack()
    lb5=Label(f5,bg="white")
    lb5.pack()

    
    btn1=Button(f1,image=ing_chonanh,bd=0,highlightthickness=0,command=lambda:chonanh(lb1,1,btn1))
    btn1.pack(side="bottom")
    btn2=Button(f2,image=ing_chonanh,bd=0,highlightthickness=0,command=lambda:chonanh(lb2,2,btn2))
    btn2.pack(side="bottom")
    btn3=Button(f3,image=ing_chonanh,bd=0,highlightthickness=0,command=lambda:chonanh(lb3,3,btn3))
    btn3.pack(side="bottom")
    btn4=Button(f4,image=ing_chonanh,bd=0,highlightthickness=0,command=lambda:chonanh(lb4,4,btn4))
    btn4.pack(side="bottom")
    btn5=Button(f5,image=ing_chonanh,bd=0,highlightthickness=0,command=lambda:chonanh(lb5,5,btn5))
    btn5.pack(side="bottom")

    
    resetanh()

    tv = ttk.Treeview(bg, columns=(1,2,3), show="headings")
    tv.column(1, width=100,anchor=CENTER)
    tv.column(2, width=100,anchor=CENTER)
    tv.column(3, width=240)
    

    tv.heading(1,text="STT")
    tv.heading(2,text="Mã sinh viên")
    tv.heading(3,text="Tên sinh viên")
    
    
    tv.place(x=368,y=350)

    tv.bind('<Double 1>', getrow)

    khoiphuc()

    win.mainloop()

