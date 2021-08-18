import mysql.connector
from tkinter import messagebox
from csdl import lop_theo_khoa
import hashlib

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="diemdanhsv"
)

cur=conn.cursor()

def banglop(makhoa):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaLop) AS STT , MaLop ,TenLop FROM lop where MaKhoa = "+str(makhoa)+"" ) 
    rows = cur.fetchall()
    conn.commit()
    return rows

def timkiem_lop(makhoa,q):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaLop) AS STT , MaLop ,TenLop FROM lop where MaKhoa = "+str(makhoa)+" AND (MaLop like '%"+str(q)+"%' OR TenLop like '%"+str(q)+"%')" ) 
    rows = cur.fetchall()
    conn.commit()
    return rows


def KT_tenlop_tontai(tenlop):
    cur.execute("SELECT TenLop FROM lop where TenLop like '%"+str(tenlop)+"%'" ) 
    rows = cur.fetchall()
    conn.commit()
    return rows

def themlop(makhoa,tenl):
    cur.execute("INSERT INTO lop(TenLop, MaKhoa) VALUES ('"+str(tenl)+"',"+str(makhoa)+")" ) 
    conn.commit()

def xoalop(malop):
    cur.execute("DELETE FROM lop WHERE MaLop="+str(malop)+"" ) 
    conn.commit()

def kt_lop_diemdanh(malop):
    cur.execute("SELECT MaLopp FROM diemdanh where MaLopp ="+str(malop)+"")
    row = cur.fetchall()
    conn.commit()
    return row

def kt_lop_tkb(malop):
    cur.execute("SELECT MaLop FROM chitiettkb where MaLop ="+str(malop)+"")
    row = cur.fetchall()
    conn.commit()
    return row

def kt_lop_sinhvien(malop):
    cur.execute("SELECT MaLop FROM sinhvien where MaLop ="+str(malop)+"")
    row = cur.fetchall()
    conn.commit()
    return row

def kt_loptontai(malop):
    if kt_lop_diemdanh(malop) != []:
        messagebox.showwarning("thông báo","Lớp vẫn còn tồn tại trong điểm danh")
        return False
    elif kt_lop_tkb(malop)!= []:
        messagebox.showwarning("thông báo","Lớp vẫn còn tồn tại trong chi tiết thời khoá biểu")
        return False
    elif kt_lop_sinhvien(malop) !=[]:
        messagebox.showwarning("thông báo","Có sinh viên tồn tại trong lớp")
        return False
    else:
        return True

def sua(malop,tenlopm):
    cur.execute("UPDATE lop SET TenLop='"+str(tenlopm)+"' WHERE MaLop="+str(malop)+"" ) 
    conn.commit()

def ma_lop_thanh_ten(ma):
    cur = conn.cursor()
    cur.execute("SELECT TenLop FROM lop where MaLop = "+str(ma)+"")
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
            
        a=row[0]
    conn.commit()
    return a







#============================================================================================================================
def DS_tkb(malop,namhoc,hki):
    cur=conn.cursor()
    cur.execute("Select Ngay, TenMH,PP_giang,TenGV,Ca FROM chitiettkb, monhoc, giangvien, lop WHERE chitiettkb.MaLop=lop.MaLop AND chitiettkb.MaMH=monhoc.MaMH AND giangvien.MaGV = chitiettkb.MaGV AND lop.MaLop ='"+str(malop)+"' AND MaNH="+str(namhoc)+" AND HocKy='"+str(hki)+"' ORDER BY Ngay" )
    rows = cur.fetchall()
    conn.commit()
    return rows

def timkiem_dongtkb(malop, q,namhoc,hki):
  cur=conn.cursor()
  cur.execute("Select Ngay, TenMH,PP_giang,TenGV,Ca FROM chitiettkb, monhoc, giangvien, lop WHERE chitiettkb.MaLop=lop.MaLop AND chitiettkb.MaMH=monhoc.MaMH AND giangvien.MaGV = chitiettkb.MaGV AND lop.MaLop ='"+str(malop)+"' AND MaNH="+str(namhoc)+" AND HocKy='"+str(hki)+"' AND (TenMH like '%"+str(q)+"%' OR  TenGV like '%"+str(q)+"%' OR Ngay like '%"+str(q)+"%' OR Ca like '%"+str(q)+"%' OR PP_giang like '%"+str(q)+"%') ")
  rows = cur.fetchall()
  conn.commit()
  return rows


def xoa_dong_tkb(ngay,monhoc,gv,ca):
  cur=conn.cursor()
  cur.execute("DELETE FROM chitiettkb WHERE Ngay like '"+str(ngay)+"' AND MaMH = "+str(monhoc)+" AND MaGV="+str(gv)+" AND Ca ='"+str(ca)+"'")
  conn.commit()

def ma_namhoc(ten):
    cur = conn.cursor()
    cur.execute("SELECT MaNH FROM namhoc where TenNH like '"+str(ten)+"'")
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
            
        a=row[0]
    conn.commit()
    return a

def them_tkb(mgv,mlop,mmh,ngay,ca,namhoc,hki,ppgiang):
  cur = conn.cursor()
  query=("INSERT INTO chitiettkb( MaGV, MaMH, MaLop, Ngay, Ca,MaNH,HocKy,PP_giang) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
  cur.execute(query,(mgv,mmh,mlop,ngay,ca,namhoc,hki,ppgiang))
  conn.commit()


def KT_lichgiang (ngay,magv,ca):
    cur = conn.cursor()
    cur.execute("SELECT MaMH FROM chitiettkb where  Ngay= '"+str(ngay)+"'  AND MaGV = "+str(magv)+" AND Ca like '%"+str(ca)+"%'")
    while True:
        row = cur.fetchone()
        if row == None:
            break
        if row[0] != []:
            return row[0]
        else:
            return 0
    conn.commit()


def KT_lich_tkb(ngay, malop,ca):
    cur = conn.cursor()
    cur.execute("SELECT MaMH FROM chitiettkb where  Ngay= '"+str(ngay)+"'  AND MaLop = "+str(malop)+" AND Ca like '%"+str(ca)+"%'")
    while True:
        row = cur.fetchone()
        if row == None:
            break
        if row[0] != []:
            return row[0]
        else:
            return 0
    conn.commit()








#=============================================================================================================================
def banggv(makhoa):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaGV) AS STT , giangvien.MaGV ,TenGV,Email,SDT, GhiChu FROM giangvien,dangnhap where dangnhap.MaGV=giangvien.MaGV AND MaKhoa = "+str(makhoa)+" AND LoaiTK='user'") 
    rows = cur.fetchall()
    conn.commit()
    return rows
def timkiem_gv(makhoa,q):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaGV) AS STT , MaGV ,TenGV,NgaySinh,Email FROM giangvien where MaKhoa = "+str(makhoa)+"  AND (MaGV='%"+str(q)+"%' OR TenGV like '%"+str(q)+"%'   OR Email like '%"+str(q)+"%')"  ) 
    rows = cur.fetchall()
    conn.commit()
    return rows
def themdangnhap(magv):
    
    hash_object = hashlib.md5(b'+magv+')
    matkhau=hash_object.hexdigest()
    cur.execute("INSERT INTO dangnhap(MaGV,MatKhau) VALUES ('"+str(magv)+"','"+str(matkhau)+"')" ) 
    conn.commit()

def KT_ma_tontai(ma):
    cur = conn.cursor()
    cur.execute("SELECT MaGV FROM giangvien where MaGV='"+str(ma)+"'")
    while True:
        row = cur.fetchone()
        if row == None:
            break
        if row[0] !=[]:
            messagebox.showwarning("thông báo"," Mã này đã tồn tại ")
            return False
        else:
            return True
    if(row==None):
        return True
    conn.commit()

def themgv(makhoa,magv,email,tengv,sdt,ghichu):
    cur.execute("INSERT INTO giangvien(MaGV,TenGV,MaKhoa,Email,SDT,GhiChu) VALUES ('"+str(magv)+"','"+str(tengv)+"' , "+str(makhoa)+", '"+str(email)+"','"+str(sdt)+"','"+str(ghichu)+"')" )
    themdangnhap(magv)
    conn.commit()

def xoatk(email):
    cur.execute("DELETE FROM dangnhap WHERE Email='"+str(email)+"'" ) 
    conn.commit()
def xoagv(magv,email):
    cur.execute("DELETE FROM giangvien WHERE MaGV="+str(magv)+"" )
    xoatk(email) 
    conn.commit()


def kt_gv_dd(magv):
    cur.execute("SELECT MaGV FROM diemdanh where MaGV ='"+str(magv)+"'")
    row = cur.fetchall()
    conn.commit()
    return row
def kt_gv_tkb(magv):
    cur.execute("SELECT MaGV FROM chitiettkb where MaGV ='"+str(magv)+"'")
    row = cur.fetchall()
    conn.commit()
    return row

def kt_gv_tontai(magv):
    if kt_gv_dd(magv) != []:
        messagebox.showwarning("thông báo","Giảng viên vẫn còn tồn tại trong điểm danh")
        return False
    elif kt_gv_tkb(magv)!= []:
        messagebox.showwarning("thông báo","Giảng viên vẫn còn tồn tại trong chi tiết thời khoá biểu")
        return False
    else:
        return True

    
def suagv(magv,tengv,sdt,ghichu):
    cur.execute("UPDATE giangvien SET TenGV='"+str(tengv)+"' , SDT = '"+str(sdt)+"', GhiChu = '"+str(ghichu)+"' WHERE MaGV = "+str(magv)+"" ) 
    conn.commit()

def bangtkb(makhoa):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaTKB) AS STT , MaTKB ,TenLop,NgayLap FROM lop,tkb where MaKhoa = "+str(makhoa)+" AND tkb.MaLop=lop.MaLop" ) 
    rows = cur.fetchall()
    conn.commit()
    return rows
def timkiem_tkb(makhoa,q):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaTKB) AS STT , MaTKB ,TenLop,NgayLap FROM lop,tkb where MaKhoa = "+str(makhoa)+" AND tkb.MaLop=lop.MaLop AND (MaTKB like '%"+str(q)+"%' OR TenLop like '%"+str(q)+"%' OR NgayLap like '%"+str(q)+"%')" ) 
    rows = cur.fetchall()
    conn.commit()
    return rows
def themtkb(malop,ngaylap):
    cur.execute("INSERT INTO tkb(MaLop, NgayLap) VALUES ("+str(malop)+",'"+str(ngaylap)+"')")
    conn.commit()
def xoatkb(matkb):
    cur.execute("DELETE FROM tkb WHERE MaTKB="+str(matkb)+"" )
    conn.commit()
def kt_chitiettkb(matkb):# kiểm tra ma thòi khoá biểu có trong chi tiết thời khoá biểu hay không
    cur.execute("SELECT MaTKB FROM chitiettkb where MaTKB = "+str(matkb)+"" ) 
    rows = cur.fetchall()
    conn.commit()
    return rows
def suatkb(matkb,malop):
    cur.execute("UPDATE tkb SET MaLop='"+str(malop)+"' WHERE MaTKB="+str(matkb)+"" ) 
    conn.commit()


    #------------------------------BẢNG MÔN HỌC ----------------------------------------------------

def bangmon(makhoa):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaMH) AS STT , MaMH ,TenMH,SoTietLT,SoTietTH FROM monhoc where MaKhoa = "+str(makhoa)+"" ) 
    rows = cur.fetchall()
    conn.commit()
    return rows

def timmon(makhoa,q):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaMH) AS STT , MaMH ,TenMH, SoTietLT,SoTietTH FROM monhoc where MaKhoa = "+str(makhoa)+" AND (MaMH like'%"+str(q)+"%' OR TenMH like'%"+str(q)+"%' OR SoTietLT like '%"+str(q)+"%' OR SoTietTH like '%"+str(q)+"%')" ) 
    rows = cur.fetchall()
    conn.commit()
    return rows

def themmon(mamh,makhoa,tenmon,lt,th):
    cur.execute("INSERT INTO monhoc(MaMH,TenMH, MaKhoa,SoTietLT,SoTietTH) VALUES ('"+str(mamh)+"','"+str(tenmon)+"',"+str(makhoa)+","+str(lt)+","+str(th)+")" ) 
    conn.commit()

def xoamon(mamh):
    cur.execute("DELETE FROM monhoc WHERE MaMH='"+str(mamh)+"'" ) 
    conn.commit()

def suamon(mamon,tenmon,lt,th):
    cur.execute("UPDATE monhoc SET TenMH='"+str(tenmon)+"' , SoTietLT="+str(lt)+" , SoTietTH="+str(th)+" WHERE MaMH="+str(mamon)+"" ) 
    conn.commit()

def kt_ma_mh(mamh):
    cur.execute("SELECT MaMH FROM monhoc where MaMH ='"+str(mamh)+"' ")
    row = cur.fetchall()
    conn.commit()
    return row

def kt_ten_mh(tenmh):
    cur.execute("SELECT MaMH FROM monhoc where TenMH like '"+str(tenmh)+"' ")
    a=None
    try:
        while True:
            row = cur.fetchone()
            if row == None:
                break
            a=row[0]
    except:
        a=None
    conn.commit()
    return a

print(kt_ten_mh("lập trình game"))

#---------------------------------------------------------------------------------------------------------

def Ngay_DD(makhoa):
    cur = conn.cursor()
    a=lop_theo_khoa(makhoa)
    b=[]
    for i in range(len(a)):
        cur.execute("SELECT Ngay FROM diemdanh,lop WHERE diemdanh.MaLopp=lop.MaLop AND TenLop='"+str(a[i])+"'")
        while True:
            row = cur.fetchone()
            if row == None:
                break
            b.append(row)
    b=dict.fromkeys(b)
    d=list(b)
    conn.commit()
    return d


#------------------------------năm học
def namhoc():
    cur.execute("SELECT TenNH FROM namhoc")
    a=[]
    while True:
        row = cur.fetchone()
        if row == None:
            break
        a.append(row[0])
    conn.commit()
    return a
