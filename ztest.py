
# import pickle
# # cv2.imwrite('dataSet/User.'+str(id)+'.'+str(sampleNum)+'.png',gray[y: y+h, x: x+w])

# f=open("mahoa/Cong_nghe_thong_tin_k19mahoa.pkl","rb")
# ref_dictt=pickle.load(f)
# print(ref_dictt)
# f.close()

# # thiết kế trang khi không có dữ liệu

import mysql.connector
import xlrd
import pandas as pd



conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="diemdanhsv"
)


cur=conn.cursor()

import pandas as pd
xl = pd.ExcelFile('sinhvien.xlsx')
df = pd.read_excel(xl, 0) 


for i in range(df.shape[0]):
    ma=df['Mã sinh viên'][i]
    ten=df['Tên sinh viên'][i]
    cur.execute("INSERT INTO sinhvien(MaSV,TenSV) VALUES ("+str(ma)+",'"+str(ten)+"')")
    
   


conn.commit()
conn.close()






