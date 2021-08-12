import socket
import diemdanhsv
import dangnhap
import csdl
import admin_lop

def main():
    ten_thiet_bi = socket.gethostname()

    file=open(ten_thiet_bi+".txt","a")
    file.close()

    data=[]
    with open(ten_thiet_bi+".txt","r") as file:
        data= file.read().split("\n")
    if data[0] != "":
        if csdl.KT_loaitk(data[0]) == "add":
            admin_lop.main()
        else:
            diemdanhsv.main()
    else:
        dangnhap.main()


if __name__ == '__main__':
    main()