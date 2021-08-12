
# import pickle
# # cv2.imwrite('dataSet/User.'+str(id)+'.'+str(sampleNum)+'.png',gray[y: y+h, x: x+w])



# from datetime import datetime
# import time

# tgbd = datetime.now()
# # t = tgbd.strftime("%H:%M:%S")
# time.sleep(5)
# # now = datetime.now()
# # k = now.strftime("%H:%M:%S")

# # a=now-tgbd

# now =datetime.now()
# s=now-tgbd
# print(s)
# def doigiay(s):
#         h=str(s)[0:1]
#         p=str(s)[2:4]
#         s=str(s)[5:7]
#         giay=int(h)*60*60+int(p)*60+int(s)
#         return giay

# if doigiay(s)<= 5:
#       print("trể "+str(s)[0:7])
import pickle


f=open("mahoa/Cong_nghe_thong_tin_k19mahoa.pkl","rb")
ref_dictt=pickle.load(f) #đọc file và luu tên theo id vào biến ref_dictt
f.close()

print(ref_dictt)