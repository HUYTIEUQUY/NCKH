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

