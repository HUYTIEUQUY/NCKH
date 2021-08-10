
# import pickle
# # cv2.imwrite('dataSet/User.'+str(id)+'.'+str(sampleNum)+'.png',gray[y: y+h, x: x+w])

# f=open("mahoa/Cong_nghe_thong_tin_k19mahoa.pkl","rb")
# ref_dictt=pickle.load(f)
# print(ref_dictt)
# f.close()

# # thiết kế trang khi không có dữ liệu

import mysql.connector
import socket 
import datetime

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="diemdanhsv"
)


cur=conn.cursor()


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


print(makhoa_tu_email("admincntt@gmail.com"))