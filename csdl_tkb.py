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

