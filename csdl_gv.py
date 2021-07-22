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

