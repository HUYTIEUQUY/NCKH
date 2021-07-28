import pickle
import shutil

f=open("mahoa/Cong_nghe_thong_tin_k19mahoa.pkl","rb")
ref_dictt=pickle.load(f)
print(ref_dictt)
f.close()


# shutil.copyfile('C:/Users/Dell/Pictures/Camera Roll/a.jpg','./img/a.jpg')

# ref_dictt.pop('114')
# capnhat={}
# capnhat[114]=ref_dictt.get('114')

# f=open("mahoa/Cong_nghe_thong_tin_k19mahoa.pkl","wb+")
# ref_dictt=pickle.load(f)
# capnhat=ref_dictt.pop("117")
# pickle.dump(capnhat,f)
# f.close()

# with open("mahoa/Cong_nghe_thong_tin_k19mahoa.pkl","rb") as f:
#     ref_dictt=pickle.load(f)
#     capnhat=ref_dictt.pop("114")

# del ref_dictt[2]

# file= open("mahoa/Cong_nghe_thong_tin_k19mahoa.pkl","wb") 
# pickle.dump(ref_dictt,file)

# with open("mahoa/Cong_nghe_thong_tin_K19mahoa.pkl","rb") as f:
#     ref_dictt=pickle.load(f)
# 
# capnhat=ref_dictt.keys()
# print(capnhat)