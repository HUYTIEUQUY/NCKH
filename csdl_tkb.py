import mysql.connector
from mysql.connector import cursor
import datetime
import csdl

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="diemdanhsinhvien"
)

def DS_tkb(matkb):
    cur=conn.cursor()
    cur.execute("SELECT Ngay, TenMH,TenGV,Ca FROM chitiettkb, monhoc, giangvien WHERE chitiettkb.MaMH=monhoc.MaMH AND giangvien.MaGV = chitiettkb.MaGV AND MaTKB ="+str(matkb)+" ORDER BY Ca" )
    rows = cur.fetchall()
    return rows

def timkiem_tkb(q):
  cur=conn.cursor()
  cur.execute("SELECT Ngay,TenMH, TenGV,Ca FROM chitiettkb, monhoc, giangvien WHERE chitiettkb.MaMH=monhoc.MaMH AND giangvien.MaGV = chitiettkb.MaGV AND (TenMH like '%"+str(q)+"%' OR  TenGV like '%"+str(q)+"%' OR Ngay like '%"+str(q)+"%' OR Ca like '%"+str(q)+"%')")
  rows = cur.fetchall()
  return rows

def xoa_dong_ds(ngay,monhoc,gv,ca):
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


