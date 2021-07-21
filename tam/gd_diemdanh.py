from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox
import os
import face_recognition
import csdl
import pickle
import cv2
import numpy as np
import socket
import wikipedia
from gtts import gTTS
import playsound
from webdriver_manager . chrome import ChromeDriverManager




def giao_dien_dd():
    wikipedia.set_lang('vi')
    language ='vi'
    path = ChromeDriverManager().install()

    def speak(text):
        tts = gTTS(text=text,lang=language,slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3", True)
        os.remove("sound.mp3")
   
    def diemdanh():
        messagebox.showwarning("thông báo","Nhấn 'q' để thoát ")
        malop=csdl.tenlop_thanh_ma(data_lop)
        a=csdl.lay_id_theo_lop(malop)#------------------lấy id theo lop
        lopp=data_lop.replace(" ","_")
        f=open("mahoa/"+lopp+".pkl","rb")
        ref_dictt=pickle.load(f) #đọc file và luu tên theo id vào biến ref_dictt
        f.close()
        f=open("mahoa/"+lopp+"mahoa.pkl","rb")
        embed_dictt=pickle.load(f) #đọc file và luu hình ảnh đã biết được mã hoá  theo id vào biến embed_dictt
        f.close()

        known_face_encodings = []  
        known_face_names = []  

        for ref_id , embed_list in embed_dictt.items():
            for my_embed in embed_list:
                known_face_encodings +=[my_embed]
                known_face_names += [ref_id]

        video_capture  = cv2.VideoCapture(0)
        face_locations = []
        face_encodings = []
        face_names     = []
        diemdanh       =[]
        process_this_frame = True #xử lý khung
        while True  :
        
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1] # Chuyển đổi hình ảnh từ màu BGR (OpenCV sử dụng) sang màu RGB (face_recognition sử dụng)
            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)# tìm tất cả khuôn mặt trong khung hình hiện tại vủa video
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) #mã hoá khuôn mặt hiện tại trong khung hình của video
                face_names = []
                for face_encoding in face_encodings:
                    # Xem khuôn mặt có khớt cới các khuôn mặt đã biết không
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                    #Đưa ra các khoảng cách giữa các khuôn mặt và khuôn mặt đã biết
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances) #Cái nào gần hơn thì lưu vào biến best_match_index
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                        
                    face_names.append(name)
                    if name not in diemdanh:
                        speak(ref_dictt[name]+" đã điểm danh")
                        diemdanh.append(name)
            process_this_frame = not process_this_frame
            

            #Hiển thị kết quả
            for (top_s, right, bottom, left), name in zip(face_locations, face_names):
                top_s *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top_s), (right, bottom), (255,0, 0), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255,0, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                if name == "Unknown":
                    cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 0,255), 2)
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0,255), cv2.FILLED)
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
                else:
                    cv2.putText(frame, ref_dictt[name], (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 1)
                
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()

        #----------------------------------------------------------------------------
        malop=csdl.tenlop_thanh_ma(data_lop)
        mamh=csdl.tenmon_thanh_ma(data_mon)
        magv=csdl.tim_magv_tu_email()
        ca=csdl.cahoc()
        csdl.diem_danh_vao_csdl(a,diemdanh,malop,mamh,magv,ca)
        csdl.update_TT_diemdanh(malop,mamh,magv)
        
        row=csdl.bangdiemdanh(malop,mamh,ca)
        tengiangvien=csdl.tim_tengv_tu_email()
        Label(lf_2,text="Giảng viên điểm danh: "+str(tengiangvien), font=("Times new roman",12,"bold")).grid(row=0,column=0)
        tv = ttk.Treeview(lf_2, columns=(1,2,3), show="headings")
        tv.grid(row=1,column=0,padx=90, pady=20)
        tv.heading(1,text="Tên Sinh Viên" )
        tv.heading(2,text="Điểm danh")
        tv.heading(3,text="Môn học")
        for i in row:
            tv.insert('','end',values=i)

    #---------------------------------------------
    def kt ():
        mlop=csdl.tenlop_thanh_ma(data_lop)
        mmh=csdl.tenmon_thanh_ma(data_mon)
        mgv=csdl.tim_magv_tu_email()
        
        if data_lop == "Bạn không có tiết dạy !":
            messagebox.showwarning("thông báo","Bạn không có tiết dạy")
            win.destroy()
            home.home()
        elif csdl.kt_dd(mlop,mmh,mgv) == "chưa":
            diemdanh()
        else:
            messagebox.showwarning("thông báo","Đã điểm danh rồi !")

    def trolai():
        win.destroy()
        home.home()

    #-----------------------------------------
    win =Tk()
    win.title("Phần mền điểm danh bằng nhận dạng khuôn mặt ")
    win.geometry("800x750")
    win.resizable(False,False)
    Label(win, text="Điểm Danh",fg="Blue",font=("Times new roman",30)).pack( pady=20)

 

    lf=LabelFrame(win,text="Lấy thông tin điểm danh", width=200,height=10)
    lf.pack( padx=20, pady=10,fill="both",)

    f1 = Frame(lf)
    f1.pack(pady=20)

    lb=Label(f1,text="Môn học",font=("Time new roman",15,"bold"))
    lb.grid(row=1,column=0,pady=25)

    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    makhoa=csdl.makhoa_tu_email(d[0])
    ma_gv=csdl.tim_magv_tu_email()
    ca=csdl.cahoc()
    if csdl.hien_mon_theo_tkb(ma_gv,ca) == []:
        data_mon="Bạn không có tiết dạy !"
    else:
        data_mon=csdl.hien_mon_theo_tkb(ma_gv,ca)
    cb_mon=Label(f1,width=30,text=data_mon,font=("Time new roman",15))
    cb_mon.grid(row=1,column=2)

    lb_lop=Label(f1,text="Lớp ",font=("Time new roman",15,"bold"))
    lb_lop.grid(row=0,column=0)

    if(csdl.hien_lop_theo_tkb(ma_gv,ca) == []):
        data_lop="Bạn không có tiết dạy !"
    else:
        data_lop = csdl.hien_lop_theo_tkb(ma_gv,ca)
    cb_lop=Label(f1,width=30,text=data_lop,font=("Time new roman",15))
    cb_lop.grid(row=0,column=2)

    Frame(f1, width=40,height=40).grid(row=0,column=1,rowspan=2,padx=20)

    Button(lf,text="Bắt đầu điểm danh sinh viên",command=kt ,font=("Time new roman",15),bg="blue",fg="white").pack(pady=10)
   
    lf_2 = LabelFrame(win,text="Bảng điểm danh" ,width=500,height=300)
    lf_2.pack(padx=20, pady=10,fill="both")

    Button(win,text="Trở lại", font=("Time new roman",15),command=trolai , bg="blue",fg="white").pack(pady=10)

    win.mainloop()



