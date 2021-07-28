from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os
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




def main():
    def dssv():
        win.destroy()
        dssv.main()
    def chonanh(i):
        lb=Label(f)
        lb.pack(side='left')
        if i==1:
            x=file1=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All file","*.*")))
        elif i==2:
            x=file2=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All file","*.*")))
        elif i==3:
            x=file3=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All file","*.*")))
        else:
            x=file4=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All file","*.*")))

        img=Image.open(x)
        img.thumbnail((150,150))
        img=ImageTk.PhotoImage(img)
        lb.config(image=img)
        lb.image=img
        if i==4:
            i=4
        else:
            i=i+1
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
    def themdlkhuonmat():
        messagebox.showinfo("thông báo","bấm s để chụp")
        
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
            #================== kết thúc hàm insertOrUpdate
        id=txt_masv.get()
        name=txt_hoten.get()
        malop=csdl.tenlop_thanh_ma(cb_lop.get())
        #thêm id , name vào co sở dữ liệu
        insertOrUpdate(id,name,malop)
        lop=cb_lop.get().replace(" ","_")
        try:
            f=open("mahoa/"+lop+".pkl","rb")
            ref_dictt=pickle.load(f)
            f.close()
        except:
            ref_dictt={}
        ref_dictt[id]=name
        f=open("mahoa/"+lop+".pkl","wb")
        pickle.dump(ref_dictt,f)
        f.close()


        try:
            f=open("mahoa/"+lop+"mahoa.pkl","rb")
            embed_dictt=pickle.load(f)
            f.close()
        except:
            embed_dictt={}


        # face_locations = face_recognition.face_locations(file1)
        # print(face_locations)

        for i in range(5):
            key = cv2. waitKey(1)
            webcam = cv2.VideoCapture(0)
            while True:
            
                check, frame = webcam.read()
                cv2.imshow("Capturing", frame)
                # Thay đổi kích thước trong opencv
                #frame: màn hình là hình ảnh đầu vào
                #(0, 0), fx=0.25, fy=0.25 : kích thước mong muốn cho hình ảnh đầu
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = small_frame[:, :, ::-1] # Chuyển đổi hình ảnh từ màu BGR (OpenCV sử dụng) sang màu RGB (face_recognition sử dụng)
        
                key = cv2.waitKey(1)
                if key == ord('s') : 
                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    if face_locations != []: #nếu có khuôn mặt
                        face_encoding = face_recognition.face_encodings(frame)[0] #mã hoá và lưu vào biến face_encoding
                        if id in embed_dictt: #Nếu id đã tồn tại thì cộng thêm hình ảnh đã mã hoá vào
                            embed_dictt[id]+=[face_encoding]
                        else:#Nếu chưa tồn tại thì khởi tạo với "id"="dữ liệu hình ảnh mã hoá"
                            embed_dictt[id]=[face_encoding]
                        if(i==4):
                            messagebox.showinfo("thông báo", "Đã lưu mã hoá khuôn mặt")
                        webcam.release()
                        
                        cv2.destroyAllWindows()
                        break
                    
                elif key == ord('q'):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows() # thoát khỏi camera
                    break
                    


        f=open("mahoa/"+lop+"mahoa.pkl","wb")
        pickle.dump(embed_dictt,f)
        f.close()

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
    ing_frame=ImageTk.PhotoImage(file="img/frame.png")
    ing_dssv=ImageTk.PhotoImage(file="img/danhsachsinhvien.png")

    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    #chọn lớp
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    makhoa=csdl.makhoa_tu_email(d[0])
    data_lop=csdl.lop_theo_khoa(makhoa)
    file1=StringVar()
    file2=StringVar()
    file3=StringVar()
    file4=StringVar()





    cb_lop=Combobox(bg,width=27,values=data_lop, font=("Baloo Tamma",12))
    cb_lop.current(0)
    cb_lop.place(x=580,y=90)
    Frame(bg,width=280,height=5,bg= "white").place(x=570,y=90)
    Frame(bg,width=276,height=5,bg= "white").place(x=570,y=112)
    Frame(bg,width=5,height=20,bg= "white").place(x=577,y=90)

    txt_masv=Entry(bg,width=30,bd=0,font=("Baloo Tamma",12))
    txt_masv.place(x=578,y=140)

    txt_hoten=Entry(bg,width=30,bd=0,font=("Baloo Tamma",12))
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

    btndssv=Button(bg,image=ing_dssv,bd=0,highlightthickness=0,command=dssv)
    btndssv.place(x=949,y=2)

    tengv=csdl.tim_tengv_tu_email()
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)
    # i=1
    # Button(bg,image=ing_btnchonanh,bd=0,highlightthickness=0,command=lambda:chonanh(i)).place(x=583,y=281)

    f=Frame(bg)
    f.place(x=330,y=330)
    Label(bg,image=ing_frame,bd=0,highlightthickness=0).place(x=389,y=229)


    


    win.mainloop()

