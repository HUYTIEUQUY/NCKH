import mysql.connector
import socket 
import datetime

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="diemdanhsinhvien"
)


cur=conn.cursor()

def banglop(makhoa):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaLop) AS STT , MaLop ,TenLop FROM lop where MaKhoa = "+str(makhoa)+"" ) 
    rows = cur.fetchall()
    return rows
def timkiem_lop(makhoa,q):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaLop) AS STT , MaLop ,TenLop FROM lop where MaKhoa = "+str(makhoa)+" AND (MaLop like '%"+str(q)+"%' OR TenLop like '%"+str(q)+"%')" ) 
    rows = cur.fetchall()
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
    return row
def kt_lop_tkb(malop):
    cur.execute("SELECT MaLop FROM chitiettkb where MaLop ="+str(malop)+"")
    row = cur.fetchall()
    return row
def kt_lop_sinhvien(malop):
    cur.execute("SELECT MaLop FROM sinhvien where MaLop ="+str(malop)+"")
    row = cur.fetchall()
    return row

def kt_loptontai(malop):
    if (kt_lop_diemdanh(malop) == []
     and kt_lop_tkb(malop)== []
     and kt_lop_sinhvien(malop) ==[]):
      return True
    else:
      return False

def sua(malop,tenlopm):
    cur.execute("UPDATE lop SET TenLop='"+str(tenlopm)+"' WHERE MaLop="+str(malop)+"" ) 
    conn.commit()

def DS_tkb(matkb):
    cur=conn.cursor()
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY Ngay) AS STT,Ngay, TenMH,TenGV,Ca FROM chitiettkb, monhoc, giangvien WHERE chitiettkb.MaMH=monhoc.MaMH AND giangvien.MaGV = chitiettkb.MaGV AND MaTKB ="+str(matkb)+" ORDER BY Ngay" )
    rows = cur.fetchall()
    return rows

def timkiem_tkb(matkb, q):
  cur=conn.cursor()
  cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY Ngay) AS STT, Ngay,TenMH, TenGV,Ca FROM chitiettkb, monhoc, giangvien WHERE chitiettkb.MaMH=monhoc.MaMH AND giangvien.MaGV = chitiettkb.MaGV AND MaTKB ="+str(matkb)+" AND (TenMH like '%"+str(q)+"%' OR  TenGV like '%"+str(q)+"%' OR Ngay like '%"+str(q)+"%' OR Ca like '%"+str(q)+"%')")
  rows = cur.fetchall()
  return rows


def xoa_dong_tkb(ngay,monhoc,gv,ca):
  cur=conn.cursor()
  cur.execute("DELETE FROM chitiettkb WHERE Ngay like '"+str(ngay)+"' AND MaMH = "+str(monhoc)+" AND MaGV="+str(gv)+" AND Ca ='"+str(ca)+"'")
  conn.commit()


def them_tkb(matkb,mgv,mlop,mmh,ngay,ca):
  cur = conn.cursor()
  query=("INSERT INTO chitiettkb(MaTKB, MaGV, MaMH, MaLop, Ngay, Ca) VALUES (%s,%s,%s,%s,%s,%s)")
  cur.execute(query,(matkb,mgv,mmh,mlop,ngay,ca))
  conn.commit()


def ma_lop_thanh_ten(ma):
    cur = conn.cursor()
    cur.execute("SELECT * FROM lop where MaLop = "+str(ma)+"")
    while True:

        row = cur.fetchone()
        
        if row == None:
            break
            
        a=row[1]
    return a

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
def banggv(makhoa):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaGV) AS STT , MaGV ,TenGV,NgaySinh,Email FROM giangvien where MaKhoa = "+str(makhoa)+"" ) 
    rows = cur.fetchall()
    return rows
def timkiem_gv(makhoa,q):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaGV) AS STT , MaGV ,TenGV,NgaySinh,Email FROM giangvien where MaKhoa = "+str(makhoa)+"  AND (MaGV='%"+str(q)+"%' OR TenGV like '%"+str(q)+"%'  OR  NgaySinh like '%"+str(q)+"%'  OR Email like '%"+str(q)+"%')"  ) 
    rows = cur.fetchall()
    return rows
def themdangnhap(email,ngaysinh):
    matkhau=ngaysinh.replace("/","")
    cur.execute("INSERT INTO dangnhap(Email,MatKhau) VALUES ('"+str(email)+"','"+str(matkhau)+"')" ) 
    conn.commit()
def themgv(makhoa,email,ngaysinh,tengv):
    themdangnhap(email,ngaysinh)
    cur.execute("INSERT INTO giangvien(TenGV,MaKhoa,Email,NgaySinh) VALUES ('"+str(tengv)+"'  , "+str(makhoa)+", '"+str(email)+"', '"+str(ngaysinh)+"' )" ) 
    conn.commit()
def xoatk(email):
    cur.execute("DELETE FROM dangnhap WHERE Email='"+str(email)+"'" ) 
    conn.commit()
def xoagv(magv,email):
    cur.execute("DELETE FROM giangvien WHERE MaGV="+str(magv)+"" )
    xoatk(email) 
    conn.commit()
def kt_lop_diemdanh(malop):
    cur.execute("SELECT MaLopp FROM diemdanh where MaLopp ="+str(malop)+"")
    row = cur.fetchall()
    return row
def kt_lop_tkb(malop):
    cur.execute("SELECT MaLop FROM chitiettkb where MaLop ="+str(malop)+"")
    row = cur.fetchall()
    return row
def kt_lop_sinhvien(malop):
    cur.execute("SELECT MaLop FROM sinhvien where MaLop ="+str(malop)+"")
    row = cur.fetchall()
    return row

def kt_loptontai(malop):
    if (kt_lop_diemdanh(malop) == []
     and kt_lop_tkb(malop)== []
     and kt_lop_sinhvien(malop) ==[]):
      return True
    else:
      return False

def suagv(magv,tengv,ngaysinh):
    cur.execute("UPDATE giangvien SET TenGV='"+str(tengv)+"',NgaySinh='"+str(ngaysinh)+"' WHERE MaGV="+str(magv)+"" ) 
    conn.commit()

def bangtkb(makhoa):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaTKB) AS STT , MaTKB ,TenLop,NgayLap FROM lop,tkb where MaKhoa = "+str(makhoa)+" AND tkb.MaLop=lop.MaLop" ) 
    rows = cur.fetchall()
    return rows
def timkiem_tkb(makhoa,q):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaTKB) AS STT , MaTKB ,TenLop,NgayLap FROM lop,tkb where MaKhoa = "+str(makhoa)+" AND tkb.MaLop=lop.MaLop AND (MaTKB like '%"+str(q)+"%' OR TenLop like '%"+str(q)+"%' OR NgayLap like '%"+str(q)+"%')" ) 
    rows = cur.fetchall()
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
    return rows
def suatkb(matkb,malop):
    cur.execute("UPDATE tkb SET MaLop='"+str(malop)+"' WHERE MaTKB="+str(matkb)+"" ) 
    conn.commit()


    #------------------------------BẢNG MÔN HỌC ----------------------------------------------------

def bangmon(makhoa):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaMH) AS STT , MaMH ,TenMH FROM monhoc where MaKhoa = "+str(makhoa)+"" ) 
    rows = cur.fetchall()
    return rows

def timmon(makhoa,q):
    cur.execute("SELECT ROW_NUMBER() OVER ( ORDER BY MaMH) AS STT , MaMH ,TenMH FROM monhoc where MaKhoa = "+str(makhoa)+" AND (MaMH like'%"+str(q)+"%' OR TenMH like'%"+str(q)+"%')" ) 
    rows = cur.fetchall()
    return rows

def themmon(makhoa,tenmon):
    cur.execute("INSERT INTO monhoc(TenMH, MaKhoa) VALUES ('"+str(tenmon)+"',"+str(makhoa)+")" ) 
    conn.commit()
def xoamon(mamh):
    cur.execute("DELETE FROM monhoc WHERE MaMH="+str(mamh)+"" ) 
    conn.commit()

def suamon(mamon,tenmon):
    cur.execute("UPDATE monhoc SET TenMH='"+str(tenmon)+"' WHERE MaMH="+str(mamon)+"" ) 
    conn.commit()

