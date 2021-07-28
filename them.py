from tkinter import *
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




def main():
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
        with open(str(ma.get())+".txt","r") as file1:
            a=file1.read().split()

        if (len(a)=="1"):
            with open(str(ma.get())+".txt","w") as file:
                return
        else:
            a=a.pop(i)
            with open(str(ma.get())+".txt","w") as file:
                for u in range(len(a)):
                    file.write(str(a[u])+"\n")
        chonanh(lb,i,btn)
    def chonanh(lb,i,btn):
        x= filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All file","*.*")))
        shutil.copyfile(x,"./img_anhsv/"+str(ma.get())+str(i)+".png")
        with open(str(ma.get())+".txt","a") as file1:
            file1.write(str(ma.get())+str(i)+".png\n")
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
    def insertOrUpdate(id, name,malop):
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="diemdanhsinhvien"
        )
        cur = conn.cursor()
        cur.execute("select * from sinhvien where MaSV="+str(id))
        Cusror = cur.fetchall()

        isRecordExist = 0 #kiểm tra nếu có ID trong database rồi thì = 1 nếu chưa thì giữ =0
        for row in Cusror:
            isRecordExist = 1
        
        if(isRecordExist == 0):
            cur.execute("insert into sinhvien(MaSV,TenSV,MaLop) values("+str(id)+",'"+str(name)+"',"+str(malop)+")")
        else:
            status=messagebox.askyesno("Thông báo","ID đã tồn tại! Bạn có muốn update tên ?")
            if status == True:
                cur.execute("update sinhvien set TenSV='"+str(name)+"'where MaSV="+str(id))
            else:
                win.destroy()
                main()
        conn.commit()
        conn.close()
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
        
        d = []
        with open(str(ma.get())+".txt","r") as f:
            d=f.read().split()

        for i in range(len(d)):
            file1_image = face_recognition.load_image_file("img_anhsv/"+d[i])
            file1_face_encoding = face_recognition.face_encodings(file1_image)[0]
            if id in embed_dictt:
                embed_dictt[id]+=[file1_face_encoding]
            else:
                embed_dictt[id]=[file1_face_encoding]
        

        f=open("mahoa/"+lopmahoa+"mahoa.pkl","wb")
        pickle.dump(embed_dictt,f)
        f.close()
        insertOrUpdate(id,name,malop)
        os.remove(str(ma.get())+".txt")
        ma.set("")
        ten.set("")
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

        messagebox.showinfo("thông báo","Đã thêm sinh viên váo danh sách")
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
    ing_btnthem=ImageTk.PhotoImage(file="img/btnthemdulieukhuonmat.png")
    ing_btnchonanh=ImageTk.PhotoImage(file="img/chon_anh.png")
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_chonanh=ImageTk.PhotoImage(file="img/btnchhonanh.png")

    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    #chọn lớp
    ten_thiet_bi = socket.gethostname()
    d=[]
    ma=StringVar()
    ten=StringVar()

    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    makhoa=csdl.makhoa_tu_email(d[0])
    data_lop=csdl.lop_theo_khoa(makhoa)





    cb_lop=Combobox(bg,width=27,values=data_lop, font=("Baloo Tamma",12))
    cb_lop.current(0)
    cb_lop.place(x=580,y=90)
    Frame(bg,width=287,height=5,bg= "white").place(x=570,y=90)
    Frame(bg,width=276,height=5,bg= "white").place(x=570,y=110)
    Frame(bg,width=5,height=20,bg= "white").place(x=577,y=90)

    
    txt_masv=Entry(bg,width=30,bd=0,font=("Baloo Tamma",12),textvariable=ma)
    txt_masv.place(x=578,y=140)

    txt_hoten=Entry(bg,width=30,bd=0,font=("Baloo Tamma",12),textvariable=ten)
    txt_hoten.place(x=578,y=190)


    txt_tenmahoa=Entry(bg,width=30,bd=0,font=("Baloo Tamma",12))
    txt_tenmahoa.place(x=578,y=237)


    btnthem=Button(bg,image=ing_btnthem,bd=0,highlightthickness=0,command=themdlkhuonmat)
    btnthem.place(x=557,y=464)

    

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
    f1.place(x=322,y=323)
    f2=Frame(bg,bg="white",width=100,height=120)
    f2.place(x=458,y=323)
    f3=Frame(bg,bg="white",width=100,height=120)
    f3.place(x=594,y=323)
    f4=Frame(bg,bg="white",width=100,height=120)
    f4.place(x=730,y=323)
    f5=Frame(bg,bg="white",width=100,height=120)
    f5.place(x=866,y=323)

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


    


    win.mainloop()

main()