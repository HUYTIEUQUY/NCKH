from tkinter import messagebox
import mysql.connector
import socket 
import datetime

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="diemdanhsv"
)



def dangnhap(email,matkhau):
    cur = conn.cursor()
    cur.execute("SELECT Email, MatKhau FROM dangnhap WHERE Email like '"+str(email)+"' and MatKhau like '"+matkhau+"'")
    a=[]
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a.append(row[0])
    return a

def KT_loaitk(email):
    cur = conn.cursor()
    cur.execute("SELECT LoaiTK FROM `dangnhap` WHERE email like '"+str(email)+"'")
    a=[]
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a=row[0]
    return a


def lay_ten_bang(tenbang):
    

    cur = conn.cursor()
    cur.execute("SELECT * FROM "+str(tenbang)+"")
    a=[]
    while True:

        row = cur.fetchone()
        
        if row == None:
            break
            
        a.append(row[1])
    return a

#----------------------------------------------kết thúc hàm lay_ten_bang
def tenkhoa_thanh_ma(ten):
    
    cur = conn.cursor()
    cur.execute("SELECT MaKhoa FROM khoa Where TenKhoa Like '"+str(ten)+"'")
    a=""
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a=row[0]
    return a
#-----------------------------------------------kết thúc hàm tên khoa thành mã
def lop_theo_khoa(makhoa):
    
    cur = conn.cursor()
    cur.execute("SELECT TenLop FROM lop WHERE MaKhoa like '"+str(makhoa)+"'")
    a=[]
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a.append(row[0])
    return a
#------------------------------------------------kết thúc hàm lớp theo khoa
def tenlop_thanh_ma(ten):
    
    cur = conn.cursor()
    cur.execute("SELECT MaLop FROM lop Where TenLop Like '"+str(ten)+"'")
    a=""
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a=row[0]
    return a
#----------------------------------------------------Kết thúc hàm tenlop_thanh_ma

def mon_theo_khoa(makhoa):
    
    cur = conn.cursor()
    cur.execute("SELECT TenMH FROM monhoc WHERE MaKhoa like '"+str(makhoa)+"'")
    a=[]
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a.append(row[0])
    return a

#------------------------------------------------------------------------------------------
def tenmon_thanh_ma(ten):
    
    cur = conn.cursor()
    cur.execute("SELECT MaMH FROM monhoc Where TenMH Like '"+str(ten)+"'")
    a=""
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a=row[0]
    return a
#--------------------------------------------------------------------------------------------

def tengv_thanh_ma(ten):
    
    cur = conn.cursor()
    cur.execute("SELECT MaGV FROM giangvien Where TenGV Like '"+str(ten)+"'")
    a=""
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a=row[0]
    return a

#---------------------------------------------------------------------------------------------
def bangdiemdanh(mlop,mmon,ca,ngay):
    x=datetime.datetime.now()
    cur = conn.cursor()
    cur.execute("SELECT TenSV, DiemDanh FROM diemdanh,sinhvien,monhoc Where sinhvien.MaSV=diemdanh.MaSV AND diemdanh.MaMH=monhoc.MaMH AND Ngay like '"+str(ngay)+"' AND MaLopp=MaLop AND MaLopp="+str(mlop)+" AND monhoc.MaMH ="+str(mmon)+" AND Ca like '"+ca+"'")
    row = cur.fetchall()
    return row
#-----------------------------------------------------------------------------

def makhoa_tu_email(email):

    cur = conn.cursor()
    cur.execute("SELECT MaKhoa FROM giangvien WHERE Email like '"+str(email)+"'")
    a=[]
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a=row[0]
    return a


#-------------------------------------------------------------------------------------------
#TRUY VẤN MÃ GIẢNG VIÊN THEO EMAIL
def tim_magv_tu_email():
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    cur = conn.cursor()
    cur.execute("SELECT MaGV FROM giangvien WHERE Email like '"+str(d[0])+"'")
    a=[]
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a=row[0]
    return a
#-------------------------------------------------------------------------------------------
def tim_tengv_tu_email():
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    
    cur = conn.cursor()
    cur.execute("SELECT TenGV FROM giangvien WHERE Email like '"+str(d[0])+"'")
    a=[]
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a=row[0]
    return a

#------------------------------------------------------------------------------------------
def hien_lop_theo_tkb(magv,ca):
   
    x=datetime.datetime.now()
    cur = conn.cursor()
    cur.execute("SELECT TenLop FROM chitiettkb, lop where lop.MaLop=chitiettkb.MaLop AND Ngay like '"+dinh_dang_ngay(str(x.strftime("%x")))+"' AND MaGV="+str(magv)+" AND Ca like '%"+str(ca)+"%'")
    a=[]
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        if row[0] not in a:
            a=row[0]
    return a
        
#---------------------------------------------------------------------------------------------------
def hien_mon_theo_tkb(magv, ca):
    x=datetime.datetime.now()
    cur = conn.cursor()
    cur.execute("SELECT TenMH FROM chitiettkb, monhoc where monhoc.MaMH=chitiettkb.MaMH AND MaGV="+str(magv)+" AND Ca like '%"+str(ca)+"%' AND Ngay like '"+dinh_dang_ngay(str(x.strftime("%x")))+"'" )
    a=[]
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        if row[0] not in a:
            a= row[0]
    return a


#------------------------------------------------------------------------------------------------
def lay_id_theo_lop(malop):#lấy danh sách sinh viên theo lớp dựa vào mã lớp

        
    cur = conn.cursor()
    cur.execute("SELECT * FROM sinhvien WHERE MaLop like '"+str(malop)+"'")
    a=[]
    while True:
    
        row = cur.fetchone()
        
        if row == None:
            break
            
        a.append(row[0])
    return a
#---------------------------------------------------------------------------------------------
def diem_danh_vao_csdl(a,b,malop,mamh,magv,ca,ngay):
    c=[]
    for i in range(0,len(a)):
        if a[i] in b:
            c.append("có")
        else:
            c.append("vắng")
    cur = conn.cursor()
    for i in range(0,len(a)):
        cur.execute("Insert into diemdanh(MaSV,DiemDanh,Ngay,MaLopp,MaMH,MaGV,Ca) values ("+str(a[i])+",'"+str(c[i])+"','"+str(ngay)+"',"+str(malop)+","+str(mamh)+", "+str(magv)+" ,'"+str(ca)+"')")
    conn.commit()
#--------------------------------------------------------------------kết thúc hàm diem_danh_vao_csdl
def kt_dd(malop,mamh,mgv):
    cur = conn.cursor()
    x=datetime.datetime.now()
    cur.execute("SELECT TrangThaiDD FROM chitiettkb where MaMH="+str(mamh)+" AND Ngay ='"+dinh_dang_ngay(str(x.strftime("%x")))+"' AND MaLop="+str(malop)+" AND MaGV="+str(mgv)+"")
    a=[]
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a=row[0]
    return a
def update_TT_diemdanh(malop,mamh,magv,ngay):
    cur = conn.cursor()
    a="có"
    cur.execute("UPDATE chitiettkb set TrangThaiDD ='"+str(a)+"' WHERE MaGV="+str(magv)+" AND MaMH="+str(mamh)+" AND MaLop="+str(malop)+" AND Ngay='"+ngay+"'")
    conn.commit()
#------------------------------------------------------------------------------
def cahoc():
    now = datetime.datetime.now()
    today7h30 = now.replace(hour=7, minute=30, second=0, microsecond=0)
    today9h30 = now.replace(hour=9, minute=30, second=0, microsecond=0)
    today11h45 = now.replace(hour=12, minute=45, second=0, microsecond=0)
    today13h00 = now.replace(hour=13, minute=00, second=0, microsecond=0)
    today15h20 = now.replace(hour=15, minute=20, second=0, microsecond=0)
    today17h20 = now.replace(hour=17, minute=20, second=0, microsecond=0)
    if now>=today7h30 and now <= today9h30:
        return "1"
    elif now >= today9h30 and now<= today11h45:
        return "2"
    elif now >= today13h00 and now<= today15h20:
        return "3"
    elif now >= today15h20 and now<= today17h20:
        return "4"
    else:
        return "ca không hợp lệ"
#-----------------------------------------------------------------------------------------------
def tim_gv_trong_khoa(makhoa):
    cur = conn.cursor()
    cur.execute("SELECT TenGV FROM giangvien WHERE MaKhoa like '"+str(makhoa)+"'")
    a=[]
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a.append(row[0])
    return a
#-----------------------------------------------------------------------------------------------------
def KT_MaTKB(mlop):
    cur = conn.cursor()
    now = datetime.datetime.now()
    ngay=dinh_dang_ngay(now.strftime("%x"))
    matkb=ngay.replace("/","")
    cur.execute("SELECT MaTKB FROM tkb WHERE MaTKB = '"+str(matkb)+str(mlop)+"'")
    a=[]
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a.append(row[0])
    return a
#-----------------------------------------------------------------------------------------
def tao_tkb(mlop):
    cur = conn.cursor()
    now = datetime.datetime.now()
    ngay=dinh_dang_ngay(now.strftime("%x"))
    matkb=ngay.replace("/","")
    with open("matkb.txt","w") as f:
        f.write(str(matkb)+str(mlop)+"\n")
        f.write(str(mlop))
    cur.execute("INSERT INTO tkb(MaTKB, MaLop, NgayLap) VALUES ("+str(matkb)+str(mlop)+","+str(mlop)+",'"+str(ngay)+"')")
    conn.commit()
#-----------------------------------------------------------------------------------------------------
def bangtkb(matkb):
    cur = conn.cursor()
    cur.execute("SELECT TenMH, TenGV,Ngay,Ca FROM chitiettkb, monhoc, giangvien WHERE chitiettkb.MaMH=monhoc.MaMH AND giangvien.MaGV = chitiettkb.MaGV AND MaTKB ="+str(matkb)+"")
    row = cur.fetchall()
    return row


def dinh_dang_ngay(ngay):
    ngay=str(ngay).replace("/"," ")
    d=ngay.split()
    if len(d[0])==1:
        d[0]="0"+d[0]
    if len(d[1])==1:
        d[1]="0"+d[1]
    if len(d[2]) ==4 :
        ngay=d[0]+"/"+d[1]+"/"+d[2]
    else:
        ngay=d[1]+"/"+d[0]+"/20"+d[2]
        
    return ngay

def xoadiemdanh(malop,mamh,mgv,ca):
    ngay= datetime.datetime.now()
    ngay=dinh_dang_ngay(ngay.strftime("%x"))
    cur=conn.cursor()
    cur.execute("DELETE FROM diemdanh WHERE Ngay like '"+str(ngay)+"' AND MaMH = "+str(mamh)+" AND MaGV="+str(mgv)+" AND Ca ='"+str(ca)+"' AND MaLopp= "+str(malop)+"")
    conn.commit()

#----------------------------------------------------
def tenkhoatuma(ma):
    cur = conn.cursor()
    cur.execute("SELECT TenKhoa FROM khoa Where MaKhoa Like '"+str(ma)+"'")
    a=""
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        a=row[0]
    return a

def ngay():
    now = datetime.datetime.now()
    ngay=dinh_dang_ngay(now.strftime("%x"))
    return ngay

def cagiang(magv,l,m,c):
    cur = conn.cursor()
    cur.execute("SELECT TenLop, TenMH,Ca FROM chitiettkb, monhoc, lop WHERE chitiettkb.MaMH=monhoc.MaMH AND lop.MaLop = chitiettkb.MaLop AND MaGV ="+str(magv)+" AND Ngay = '"+str(ngay())+"'")
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        l.append(row[0])
        m.append(row[1])
        c.append(row[2])
    if l != []:
        return True
    else:
        return False

def gvdiemdanh(magv,ngaydd,tenlopdd,tenmhdd,cadd):
    cur = conn.cursor()
    cur.execute("SELECT Ngay, TenLop,TenMH,Ca FROM chitiettkb, monhoc, lop WHERE chitiettkb.MaMH=monhoc.MaMH AND lop.MaLop = chitiettkb.MaLop AND MaGV ="+str(magv)+" AND TrangThaiDD like 'chưa' AND Ngay < '"+str(ngay())+"'")
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
        ngaydd.append(row[0])
        tenlopdd.append(row[1])
        tenmhdd.append(row[2])
        cadd.append(row[3])
    if ngaydd != []:
        return True
    else:
        return False



def diemdanhbu(magv):
    cur = conn.cursor()
    cur.execute("SELECT Ngay, TenLop,TenMH,Ca FROM chitiettkb, monhoc, lop WHERE chitiettkb.MaMH=monhoc.MaMH AND lop.MaLop = chitiettkb.MaLop AND MaGV ="+str(magv)+" AND TrangThaiDD like 'chưa' AND Ngay <= '"+str(ngay())+"'")
    row = cur.fetchall()
    return row

def tim_lop_trong_diemdanh(MaGV):
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT TenLop FROM lop, diemdanh WHERE MaLop=MaLopp AND MaGV='"+str(MaGV)+"'")
    a=[]
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a.append(row[0])
    return a

def tim_mon_trong_diemdanh(MaGV,malop):
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT TenMH FROM monhoc, diemdanh WHERE monhoc.MaMH=diemdanh.MaMH AND MaGV='"+str(MaGV)+"' AND MaLopp = "+str(malop)+"")
    a=[]
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a.append(row[0])
    return a

def tim_ngay_trong_diemdanh(MaGV,malop,mamh):
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Ngay FROM diemdanh WHERE  MaGV='"+str(MaGV)+"' AND MaLopp = "+str(malop)+" AND MaMH= "+str(mamh)+"")
    a=[]
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a.append(row[0])
    return a

def tim_ca_trong_diemdanh(MaGV,malop,mamh,ngay):
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Ca FROM diemdanh WHERE  MaGV='"+str(MaGV)+"' AND MaLopp = "+str(malop)+" AND MaMH= "+str(mamh)+" AND Ngay = '"+str(ngay)+"'")
    a=[]
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a.append(row[0])
    return a

def thongke(magv,ngay,mamh,lop,ca):
    cur = conn.cursor()
    cur.execute("SELECT sinhvien.MaSV, TenSV,DiemDanh FROM sinhvien, diemdanh WHERE diemdanh.MaSV=sinhvien.MaSV AND MaMH= "+str(mamh)+" AND MaGV ="+str(magv)+" AND Ca like '%"+str(ca)+"%' AND Ngay= '"+str(ngay)+"' AND MaLop = "+str(lop)+"")
    row = cur.fetchall()
    return row

def timkiem_diemdanh(magv,ngay,mamh,lop,ca,q):
    cur=conn.cursor()
    cur.execute("SELECT sinhvien.MaSV, TenSV,DiemDanh FROM sinhvien, diemdanh WHERE diemdanh.MaSV=sinhvien.MaSV AND MaMH= "+str(mamh)+" AND MaGV ="+str(magv)+" AND Ca like '%"+str(ca)+"%' AND Ngay= '"+str(ngay)+"' AND MaLop = "+str(lop)+" AND (sinhvien.MaSV like '%"+str(q)+"%' OR TenSV like '%"+str(q)+"%' OR DiemDanh like '%"+str(q)+"%')" ) 
    rows = cur.fetchall()
    return rows

def danhsachsinhvien(malop):
    cur=conn.cursor()
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaSV) AS STT , MaSV ,TenSV FROM sinhvien where MaLop = "+str(malop)+"" ) 
    rows = cur.fetchall()
    return rows

def xoasv(masv):
    cur=conn.cursor()
    cur.execute("DELETE FROM sinhvien WHERE MaSV="+str(masv)+"" ) 
    conn.commit()

def anh(masv):
    cur=conn.cursor()
    cur.execute("SELECT Anh FROM sinhvien where MaSV = "+str(masv)+"" ) 
    a=[]
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a.append(row[0])
    return a

def timsv(malop,q):
    cur=conn.cursor()
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaSV) AS STT , MaSV ,TenSV FROM sinhvien where MaLop = "+str(malop)+" AND (MaSV like'%"+str(q)+"%' OR TenSV like'%"+str(q)+"%')" ) 
    rows = cur.fetchall()
    return rows


def insertOrUpdate(id, name,malop,anh):
    cur = conn.cursor()
    cur.execute("select * from sinhvien where MaSV="+str(id))
    Cusror = cur.fetchall()

    isRecordExist = 0 #kiểm tra nếu có ID trong database rồi thì = 1 nếu chưa thì giữ =0
    for row in Cusror:
        isRecordExist = 1
    
    if(isRecordExist == 0):
        cur.execute("insert into sinhvien(MaSV,TenSV,MaLop,Anh) values("+str(id)+",'"+str(name)+"',"+str(malop)+",'"+str(anh)+"')")
    else:
        status=messagebox.askyesno("Thông báo","ID đã tồn tại! Bạn có muốn update tên ?")
        if status == True:
            cur.execute("update sinhvien set TenSV='"+str(name)+"'where MaSV="+str(id))
    conn.commit()

def suasv(masv,tensv,lop):
    cur=conn.cursor()
    cur.execute("update sinhvien set TenSV = '"+str(tensv)+"' ,MaLop="+str(lop)+" where MaSV="+str(masv) ) 
    conn.commit()


def tim_lop(masv):
    cur = conn.cursor()
    cur.execute("SELECT TenLop FROM lop,sinhvien WHERE lop.MaLop=sinhvien.MaLop AND MaSV="+str(masv)+"")
    a=""
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a=row[0]
    return a

def suaanh(anh,ma):
    cur=conn.cursor()
    cur.execute("update sinhvien set Anh = '"+str(anh)+"' WHERE MaSV="+str(ma)+"") 
    conn.commit()


def dong_masinhvien(malop):
    cur = conn.cursor()
    cur.execute("SELECT MaSV  FROM sinhvien WHERE MaLop = "+str(malop)+"" )
    a=[]
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a.append(row[0])
    return a

def dong_tensinhvien(malop):
    cur = conn.cursor()
    cur.execute("SELECT TenSV  FROM sinhvien WHERE MaLop = "+str(malop)+"" )
    a=[]
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a.append(row[0])
    return a
    


def nhap_excel_csdl(ma,ten,malop):
    cur = conn.cursor()
    cur.execute("INSERT INTO sinhvien(MaSV,TenSV,MaLop) VALUES ("+str(ma)+",'"+str(ten)+"', "+str(malop)+")")
    conn.commit()
  



